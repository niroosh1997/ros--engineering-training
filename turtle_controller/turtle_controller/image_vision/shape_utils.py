from cv2.typing import Moments, MatLike
import cv2
from numpy import ndarray


def get_moment_sum_of_x(moments: Moments) -> float:
    return moments["m10"]


def get_moment_sum_of_y(moments: Moments) -> float:
    return moments["m01"]


def get_moments_length(moments: Moments) -> float:
    return moments["m00"]


def get_center_of_contour_shape(shape: MatLike) -> tuple[int, int]:
    moments_of_shape = cv2.moments(shape)
    center = (
        int(get_moment_sum_of_x(moments_of_shape) / get_moments_length(moments_of_shape)),
        int(get_moment_sum_of_y(moments_of_shape) / get_moments_length(moments_of_shape)),
    )
    return center
