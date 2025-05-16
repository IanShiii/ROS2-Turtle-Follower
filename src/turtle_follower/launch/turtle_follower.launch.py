from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtle_sim = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    spawn_second_turtle = Node(
        package='turtle_follower',
        executable='spawner',
        parameters=[{
            'x': 4.0,
            'y': 4.0,
            'theta': 90.0
        }]
    )

    follower_node = Node(
        package='turtle_follower',
        executable='follower',
        name='follower'
    )

    ld.add_action(turtle_sim)
    ld.add_action(spawn_second_turtle)
    ld.add_action(follower_node)

    return ld

