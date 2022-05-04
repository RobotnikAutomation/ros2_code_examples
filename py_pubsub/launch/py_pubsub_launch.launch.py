from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start Talker Node
        Node(
            package='py_pubsub',
            executable='talker',
            output='screen'),
        # Start Listener Node
        Node(
            package='py_pubsub',
            executable='listener',
            output='screen')
    ])


'''
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([

        # Start Talker Node
        launch_ros.actions.Node(
            package='py_pubsub',
            executable='talker',
            output='screen'),

        # Start Listener Node
        launch_ros.actions.Node(
            package='py_pubsub',
            executable='listener',
            output='screen'),        
    ])

'''