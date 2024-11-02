import cv2
from turtle_controller.image_vision.shape_utils import get_center_of_contour_shape
import numpy as np


def main():

    real_image = cv2.imread("turtle_controller/turtle_controller/image_vision/photo_with_ball.jpg")
    gray_image = cv2.imread(
        "turtle_controller/turtle_controller/image_vision/photo_with_ball.jpg",
        cv2.IMREAD_GRAYSCALE,
    )
    down_width = 640
    down_height = 480
    down_points = (down_width, down_height)

    real_image = cv2.resize(real_image, down_points, interpolation=cv2.INTER_LINEAR)
    real_image1 = cv2.resize(real_image, down_points, interpolation=cv2.INTER_LINEAR)
    gray_image = cv2.resize(gray_image, down_points, interpolation=cv2.INTER_LINEAR)

    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    contours, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour_with_biggest_area = max(contours, key=cv2.contourArea)

    center = get_center_of_contour_shape(contour_with_biggest_area)

    cv2.circle(real_image, center, 2, (0, 0, 255), -1)

    cv2.imshow("result", real_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
