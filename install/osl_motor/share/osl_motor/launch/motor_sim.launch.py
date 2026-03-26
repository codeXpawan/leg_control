import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('osl_motor')
    
    knee_config = os.path.join(pkg_share, 'config', 'knee_motor.yaml')
    ankle_config = os.path.join(pkg_share, 'config', 'ankle_motor.yaml')
    
    return LaunchDescription([
        Node(
            package='osl_motor',
            executable='motor_sim',
            name='knee_motor_sim',
            parameters=[knee_config],
            output='screen'
        ),
        Node(
            package='osl_motor',
            executable='motor_sim',
            name='ankle_motor_sim',
            parameters=[ankle_config],
            output='screen'
        )
    ])
