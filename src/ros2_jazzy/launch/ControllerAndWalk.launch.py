from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
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
    return LaunchDescription([
        walker_node,
        controller_node,
        # pid_tuner_node
    ])