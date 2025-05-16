import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class Spawner(Node):
    
    def __init__(self):
        super().__init__("spawner")
        self.declare_parameter('x', 0.0)
        self.declare_parameter('y', 0.0)
        self.declare_parameter('theta', 0.0)
        self.spawn_service = self.create_client(Spawn, "/spawn")
        self.spawn_service.wait_for_service()

        self.spawn_request = Spawn.Request()
        self.spawn_request.x = self.get_parameter('x').get_parameter_value().double_value
        self.spawn_request.y = self.get_parameter('y').get_parameter_value().double_value
        self.spawn_request.theta = self.get_parameter('theta').get_parameter_value().double_value
        self.spawn_service.call(self.spawn_request)

        self.destroy_node()
        rclpy.shutdown()
    
def main(args=None):
    rclpy.init(args=args)
    spawner = Spawner()
    rclpy.spin(spawner)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    