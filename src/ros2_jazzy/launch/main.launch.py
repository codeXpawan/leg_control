from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.descriptions import ParameterValue
from launch.event_handlers import OnProcessExit
import os

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default=True)
    oslsim_share = get_package_share_directory('ros2_jazzy')

    # Robot description as xacro command (for robot_state_publisher)
    robot_description = ParameterValue(
        Command(['xacro ', PathJoinSubstitution([oslsim_share, 'urdf/newoslsim.xacro']),
                 ' mesh_dir:=', "package://ros2_jazzy"]),
        value_type=str
    )

    world_path = os.path.join(oslsim_share,'worlds','main.world')

    # Gazebo launch
    ros_gz_sim = get_package_share_directory('ros_gz_sim')
    gz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': f'-r -v4 empty.sdf --render-engine ogre'}.items()
    )
    urdf_spawner = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'oslsim',
            '-string', Command(['xacro ', os.path.join(oslsim_share, 'urdf/newoslsim.xacro'), 
                                ' mesh_dir:=', os.path.join(oslsim_share,)]),
            '-x', '0', '-y', '0.005', '-z', '0.89'
        ],
        output='screen'
    )
    robot_controllers = os.path.join(oslsim_share, 'config', 'controllers.yaml')

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
    )

    # leg_controller_spawner = Node(
    #     package='controller_manager',
    #     executable='spawner',
    #     arguments=[
    #         'leg_controller',
    #         '--param-file',
    #         robot_controllers,
    #         '--controller-ros-args',
    #         '-r /leg_controller/tf_odometry:=/tf',
    #     ],
    # )

    joint_controllers = [
    'hip_position_controller',
    'osl_hip_position_controller',
    'knee_position_controller',
    'osl_knee_controller',
    'ankle_position_controller',
    'osl_ankle_controller'
    ]

    # Create a list to hold the spawner nodes
    controller_spawners = []

    for controller in joint_controllers:
        controller_spawners.append(
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=[controller],
            )
        )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'],
        output='screen'
        
    )


    # Robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'robot_description': robot_description,
                     'publish_frequency': 50.0,
                     'ignore_timestamp': True,
                     'tf_prefix': 'oslsim'}],
        # remappings=[('/joint_states', '/oslsim/joint_states')],
        output='screen'
    )

    msg_bridges = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/imu/foot@sensor_msgs/msg/Imu@gz.msgs.IMU',
            '/imu/osl_shank@sensor_msgs/msg/Imu@gz.msgs.IMU',
            '/foot/touched@std_msgs/msg/Bool@gz.msgs.Boolean',
            '/oslsim/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/model/oslsim/odometry_with_covariance@nav_msgs/msg/Odometry@gz.msgs.OdometryWithCovariance',
            '/model/oslsim/tf@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V',
            '/world/empty/model/oslsim/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/world/empty/model/oslsim/link/osl_foot/sensor/sensor_contact/contact@ros_gz_interfaces/msg/Contacts@gz.msgs.Contacts',
            '/loadcell/osl_foot@geometry_msgs/msg/Wrench@gz.msgs.Wrench'
        ],
        remappings=[
            # Stitches the Gazebo world-position onto the ROS global transform tree
            # ('/world/empty/model/oslsim/tf', '/tf'),
            # ('/world/empty/model/oslsim/joint_state', '/joint_states'),
            ('/model/oslsim/tf', '/tf'),
            ('/world/empty/model/oslsim/joint_state', '/joint_states')
            # ('/world/empty/model/oslsim/link/osl_foot/sensor/sensor_contact/contact','/osl_foot/contact')
        ],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    # Controller spawner and custom nodes
    controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        namespace='/oslsim',
        arguments=[
            'joint_state_controller',
            'hip_position_controller',
            'osl_hip_position_controller',
            'knee_position_controller',
            'ankle_position_controller'
        ],
        output='screen'
    )

    loadcell_node = Node(
        package='ros2_jazzy',
        executable='loadcell',
        output='screen'
    )

    walker_node = Node(
        package='ros2_jazzy',
        executable='oslsim_walker',
        name='oslsim_walker',
        # condition=IfCondition(LaunchConfiguration('walk'))
    )

    controller_node = Node(
        package='ros2_jazzy',
        executable='oslsim_controller',
        name='oslsim_controller',
        # condition=IfCondition(LaunchConfiguration('control'))
    )

    pid_tuner_node = Node(
        package='ros2_jazzy',
        executable='oslsim_pid_tuner',
        name='oslsim_pid_tuner',
        output='screen',
        # condition=IfCondition(LaunchConfiguration('control'))
    )

    # Motor simulation nodes — restore missing ROS1 motor layer.
    # Converts voltage commands (from controller.py) to joint torques
    # using the DC motor model from osl_knee.yaml / osl_ankle.yaml.
    knee_motor_sim = Node(
        package='osl_motor',
        executable='motor_sim',
        name='osl_knee_motor_sim',
        parameters=[os.path.join(oslsim_share, 'config', 'osl_knee.yaml'),
                   {'motor_name': 'osl_knee'}],
        remappings=[
            ('/motor_voltage/command', '/osl_knee/voltage'),
            ('/motor_effort/command', '/osl_knee_controller/commands'),
        ],
        output='screen',
        # condition=IfCondition(LaunchConfiguration('control'))
    )

    ankle_motor_sim = Node(
        package='osl_motor',
        executable='motor_sim',
        name='osl_ankle_motor_sim',
        parameters=[os.path.join(oslsim_share, 'config', 'osl_ankle.yaml'),
                   {'motor_name': 'osl_ankle'}],
        remappings=[
            ('/motor_voltage/command', '/osl_ankle/voltage'),
            ('/motor_effort/command', '/osl_ankle_controller/commands'),
        ],
        output='screen',
        # condition=IfCondition(LaunchConfiguration('control'))
    )

    return LaunchDescription([
        bridge,
        gz_launch,
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=urdf_spawner,
                on_exit=[joint_state_broadcaster_spawner],
            )
        ),
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=controller_spawners,
            )
        ),
        urdf_spawner,
        DeclareLaunchArgument(
            'use_sim_time',
            default_value=use_sim_time,
            description='If true, use simulated clock'),
        DeclareLaunchArgument(
            'description_format',
            default_value='urdf',
            description='Robot description format to use, urdf or sdf'),
        DeclareLaunchArgument(
            'walk',
            default_value='true',
            description='Enable walker node for healthy leg'),
        DeclareLaunchArgument(
            'control',
            default_value='true',
            description='Enable controller node for prosthetic leg'),
        robot_state_publisher_node,
        msg_bridges,
        # controller_spawner,
        loadcell_node,
        walker_node,
        controller_node,
        knee_motor_sim,
        ankle_motor_sim,
        # pid_tuner_node
    ])

