import cv2
from sensor_msgs.msg import Image
from turtle_controller.image_vision.shape_utils import get_center_of_contour_shape
import numpy as np


def center_of_ball(image: Image) -> tuple[int, int]:
    down_width = 640
    down_height = 480
    down_points = (down_width, down_height)

    resized_image = cv2.resize(image.data, down_points, interpolation=cv2.INTER_LINEAR)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour_with_biggest_area = max(contours, key=cv2.contourArea)

    center = get_center_of_contour_shape(contour_with_biggest_area)
