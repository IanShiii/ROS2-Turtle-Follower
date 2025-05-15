import numpy as np
import scipy
import scipy.spatial
import geometry_msgs
import geometry_msgs.msg
import rclpy
import rclpy.time
import tf2_geometry_msgs
from geometry_msgs.msg import Twist
from rclpy.node import Node
import tf2_py
import tf2_py._tf2_py
import tf2_ros
import tf2_tools
from turtlesim.msg import Pose


class Follower(Node):
    
    def __init__(self):
        super().__init__("follower")
        self.tfbuffer = tf2_ros.Buffer()
        self.follower_pose = Pose()
        self.target_pose = Pose()
        self.follower_pose_subscriber = self.create_subscription(
            Pose, 
            "/turtle2/pose", 
            self.set_follower_pose, 
            10
        )
        self.target_pose_subscriber = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.set_target_pose, 
            10
        )
        self.velocity_publisher = self.create_publisher(
            Twist,
            "/turtle2/cmd_vel",
            10
        )

    def set_follower_pose(self, pose: Pose):
        self.follower_pose = pose

    def set_target_pose(self, pose: Pose):
        self.target_pose = pose
        self.follower_to_target_turtle()

    def follower_to_target_turtle(self):
        linear_P = 2.0
        angular_P = 0.75

        velocity = Twist()

        world_x = self.target_pose.x - self.follower_pose.x
        world_y = self.target_pose.y - self.follower_pose.y

        quaternion = scipy.spatial.transform.Rotation.from_euler('xyz', [0, 0, -self.follower_pose.theta])  
        rotation_matrix = quaternion.as_matrix()

        linear_velocity = np.array([world_x, world_y, 0])

        rotated_linear_velocity = rotation_matrix @ linear_velocity

        velocity.linear.x, velocity.linear.y, velocity.linear.z = rotated_linear_velocity * linear_P
        velocity.angular.z = (self.target_pose.theta - self.follower_pose.theta) * angular_P

        self.velocity_publisher.publish(velocity)

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = Follower()
    rclpy.spin(turtle_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()