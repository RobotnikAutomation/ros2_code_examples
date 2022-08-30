from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start Listener Node
        Node(
            package='string_subscriber',
            executable='string_listener',
            output='screen')
    ])