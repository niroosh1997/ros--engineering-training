import rclpy
from geometry_msgs.msg import Twist
from turtle_controller.image_vision.ball_finding import center_of_ball_with_centuer_algorithm
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
        self.create_subscription(Image, "/camera/image_raw", self._handle_image, 10)

        self._timer = self.create_timer(0.1, self._timer_callback)

        self._movement_pid = MovmentPid(p=140, i=400, max_error=10, sample_time=0.1)
        self._current_pos = Pose()
        self._go_to_pos = Pose()

    def _timer_callback(self) -> None:
        output_twist = Twist()
        output_twist.linear.x, output_twist.linear.y = self._movement_pid.go_to(
            self._current_pos.x, self._current_pos.y, self._go_to_pos.x, self._go_to_pos.y
        )
        self._turtle_publisher.publish(output_twist)

    def _handle_turtle_pos(self, turtle_pos: Pose):
        self._current_pos = turtle_pos

    def _handle_go_to_pos(self, turtle_pos: Pose):
        self.get_logger().info(f"receive new target: {turtle_pos.x} {turtle_pos.y}")
        self._go_to_pos = turtle_pos

    def _handle_image(self, image: Image):
        x, y = center_of_ball_with_centuer_algorithm(image)

        targt_pos = Pose()
        targt_pos.x = x * 10
        targt_pos.y = 10 - y * 10
        self.get_logger().info(f"receive new target: {targt_pos.x} {targt_pos.y }")
        self._go_to_pos = targt_pos


def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
