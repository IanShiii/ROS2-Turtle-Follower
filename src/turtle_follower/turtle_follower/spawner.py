import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class Spawner(Node):
    
    def __init__(self):
        super().__init__("spawner")
        self.spawn_service = self.create_client(Spawn, "/spawn")
        self.spawn_service.wait_for_service()

        self.spawn_request = Spawn.Request()
        self.spawn_request.x = 0.0
        self.spawn_request.y = 0.0
        self.spawn_request.theta = 0.0
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
    