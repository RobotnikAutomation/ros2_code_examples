from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start Listener Node
        Node(
            package='astra_camera_subscriber',
            executable='camera_listener',
            output='screen')
    ])