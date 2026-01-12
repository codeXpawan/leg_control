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

    # Launch arguments
    walk_arg = DeclareLaunchArgument('walk', default_value='true')
    control_arg = DeclareLaunchArgument('control', default_value='true')

    # Robot description as xacro command (for robot_state_publisher)
    robot_description = ParameterValue(
        Command(['xacro ', PathJoinSubstitution([oslsim_share, 'urdf/newoslsim.xacro']),
                 ' mesh_dir:=', "package://ros2_jazzy"]),
        value_type=str
    )

    world_path = os.path.join(oslsim_share, 'worlds', 'main.world')
    # Generate URDF from XACRO for Gazebo spawn
    # urdf_file = os.path.join(oslsim_share, 'urdf', 'oslsim.urdf')
    # xacro_to_urdf = ExecuteProcess(
    #     cmd=['xacro', os.path.join(oslsim_share, 'urdf/oslsim.xacro'), '-o', urdf_file],
    #     shell=True
    # )

    # Gazebo launch
    ros_gz_sim = get_package_share_directory('ros_gz_sim')
    gz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': f'-r -v4 empty.sdf'}.items()
    )

    # Spawn robot in Gazebo using the generated URDF
#     urdf_spawner = Node(
#     package='ros_gz_sim',
#     executable='create',
#     arguments=['-topic', 'robot_description', '-name',
#                    'leg', '-allow_renaming', 'true'],
#     output='screen'
# )
    urdf_spawner = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'oslsim',
            '-string', Command(['xacro ', os.path.join(oslsim_share, 'urdf/newoslsim.xacro'), 
                                ' mesh_dir:=', os.path.join(oslsim_share,)]),
            '-x', '0', '-y', '0', '-z', '1.1'
        ],
        output='screen'
    )
    robot_controllers = os.path.join(oslsim_share, 'config', 'controllers.yaml')

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
    )

    leg_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'leg_controller',
            '--param-file',
            robot_controllers,
            '--controller-ros-args',
            '-r /leg_controller/tf_odometry:=/tf',
        ],
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

    # Bridges for joint states and IMU
    # joint_state_bridge = Node(
    #     package='ros_gz_bridge',
    #     executable='parameter_bridge',
    #     arguments=['/joint_states@sensor_msgs/msg/JointState@gz.msgs.Model'],
    #     output='screen'
    # )

    imu_bridges = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/imu/foot@sensor_msgs/msg/Imu@gz.msgs.IMU',
            '/imu/osl_shank@sensor_msgs/msg/Imu@gz.msgs.IMU',
            '/foot/touched@std_msgs/msg/Bool@gz.msgs.Boolean',
        ],
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
        condition=IfCondition(LaunchConfiguration('walk'))
    )

    controller_node = Node(
        package='ros2_jazzy',
        executable='oslsim_controller',
        name='oslsim_controller',
        condition=IfCondition(LaunchConfiguration('control'))
    )

    pid_tuner_node = Node(
        package='ros2_jazzy',
        executable='oslsim_pid_tuner',
        name='oslsim_pid_tuner',
        output='screen',
        condition=IfCondition(LaunchConfiguration('control'))
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
                on_exit=[leg_controller_spawner],
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
        # walk_arg,
        # control_arg,
        # xacro_to_urdf,  # Generate URDF before spawning
        robot_state_publisher_node,
        # joint_state_bridge,
        imu_bridges,
        # joint_state_broadcaster_spawner,
        # spawn_jsb_then_leg,
        # controller_spawner,
        # loadcell_node,
        # walker_node,
        # controller_node,
        # pid_tuner_node
    ])

