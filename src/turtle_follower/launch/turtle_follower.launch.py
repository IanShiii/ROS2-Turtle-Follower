from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtle_sim_node_1 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim1'
    )

    turtle_sim_node_2 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim2',
        remappings=[
            ("/turtle1/cmd_vel", "/turtle2/cmd_vel"),
            ("/turtle1/pose", "/turtle2/pose"),
            ("/turtle1/color_sensor", "/turtle2/color_sensor")
        ]
    )

    follower_node = Node(
        package='turtle_follower',
        executable='follower',
        name='follower'
    )

    ld.add_action(turtle_sim_node_1)
    ld.add_action(turtle_sim_node_2)
    ld.add_action(follower_node)

    return ld

