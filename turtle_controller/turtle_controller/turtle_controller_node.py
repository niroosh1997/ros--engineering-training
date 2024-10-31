import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TurtleController(Node):
    def __init__(self) -> None:
        super().__init__("TurtleController")
        self.get_logger().info("node initlized")
        self._turtle_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self._timer = self.create_timer(0.1, self._timer_callback)

    def _timer_callback(self) -> None:
        output_pose = Twist()
        # output_pose.linear.x = 5.0
        output_pose.angular.z = 3.14
        self.get_logger().info(f"published {output_pose}")
        self._turtle_publisher.publish(output_pose)


def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
