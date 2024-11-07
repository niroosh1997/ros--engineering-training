import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__("minimal_publisher")
        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)  ###### here
        self.timer = self.create_timer(2, self.timer_callback)
        self.i = 0
        self.cv_image = {}
        self.cv_image[0] = cv2.imread("./turtle_controller/turtle_controller/ball.jpg")
        self.cv_image[1] = cv2.imread("./turtle_controller/turtle_controller/ball2.jpg")
        self.cv_image[2] = cv2.imread("./turtle_controller/turtle_controller/ball3.jpg")
        self.cv_image[3] = cv2.imread("./turtle_controller/turtle_controller/ball4.jpg")
        self.bridge = CvBridge()

    def timer_callback(self):
        my_msg = self.bridge.cv2_to_imgmsg(np.array(self.cv_image[self.i]), "bgr8")
        self.publisher_.publish(my_msg)
        self.get_logger().info(f"publish image {self.i}")
        self.i = (self.i + 1) % 4


def main(args=None):

    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
