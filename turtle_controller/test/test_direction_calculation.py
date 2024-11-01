import math

from turtle_controller.direction_calculation import calculate_target_theta


def test_example():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 5.0
    target_y = 5.0
    taget_theta = calculate_target_theta(currect_x, currect_y, target_x, target_y)
    assert taget_theta == 0.75 * math.pi
