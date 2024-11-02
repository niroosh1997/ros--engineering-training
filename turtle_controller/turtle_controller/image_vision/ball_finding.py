import cv2
from sensor_msgs.msg import Image
from turtle_controller.image_vision.shape_utils import get_center_of_contour_shape
import numpy as np
from cv_bridge import CvBridge


def center_of_ball_with_centuer_algorithm(image: Image) -> tuple[float, float]:
    down_width = 640
    down_height = 480
    down_points = (down_width, down_height)

    bridge = CvBridge()
    image_cv = bridge.imgmsg_to_cv2(image)

    resized_image = cv2.resize(image_cv, down_points, interpolation=cv2.INTER_LINEAR)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour_with_biggest_area = max(contours, key=cv2.contourArea)

    center_x, center_y = get_center_of_contour_shape(contour_with_biggest_area)
    normilized_x, normilized_y = normilized_point(center_x, center_y, down_width, down_height)
    return normilized_x, normilized_y


def normilized_point(center_x, center_y, down_width, down_height) -> tuple[float, float]:
    center_x_normilized = center_x / down_width
    center_y_normilized = center_y / down_height
    return center_x_normilized, center_y_normilized
