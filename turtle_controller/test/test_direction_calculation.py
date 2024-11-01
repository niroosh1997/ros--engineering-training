import math

from turtle_controller.direction_calculation import calculate_target_theta


def test_when_in_first_square_and_x_equals_y_then_taget_theta_is_three_quarter_pi():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 5.0
    target_y = 5.0
    taget_theta = calculate_target_theta(currect_x, currect_y, target_x, target_y)
    assert taget_theta == 0.75 * math.pi

def test_when_in_forth_square_and_x_equals_y_then_taget_theta_is_quarter_pi():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 5.0
    target_y = -5.0
    taget_theta = calculate_target_theta(currect_x, currect_y, target_x, target_y)
    assert taget_theta == 0.25 * math.pi
