import rclpy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node
from sensor_msgs.msg import Image
from turtle_controller.utils.specific_pid import MovmentPid


class TurtleController(Node):
    def __init__(self) -> None:
        super().__init__("TurtleController")
        self.get_logger().info("node initlized")
        self._turtle_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_subscription(Pose, "/turtle1/pose", self._handle_turtle_pos, 10)
        self.create_subscription(Pose, "/turtle_controller/pose", self._handle_go_to_pos, 10)
        self.create_subscription(Image, "/camera/image_raw", self._handle_image)

        self._timer = self.create_timer(0.1, self._timer_callback)

        self._movement_pid = MovmentPid(p=10, i=0.2, max_error=10, sample_time=0.1)
        self._current_pos = Pose()
        self._go_to_pos = Pose()

    def _timer_callback(self) -> None:
        output_pose = Twist()
        output_pose.linear.x, output_pose.linear.y = self._movement_pid.go_to(
            self._current_pos.x, self._current_pos.y, self._go_to_pos.x, self._go_to_pos.y
        )
        self.get_logger().info(f"received {self._current_pos.x} {self._current_pos.y}")
        self.get_logger().info(f"published {output_pose.linear.x} {output_pose.linear.y}")
        self._turtle_publisher.publish(output_pose)

    def _handle_turtle_pos(self, turtle_pos: Pose):
        self._current_pos = turtle_pos

    def _handle_go_to_pos(self, turtle_pos: Pose):
        self._go_to_pos = turtle_pos

    def _handle_image(image: Image):
        pass


def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
