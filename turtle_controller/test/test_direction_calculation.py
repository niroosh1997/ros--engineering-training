import math

from turtle_controller.direction_calculation import calculate_target_theta


def test_when_deg_in_first_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 1
    target_y = math.sqrt(3)
    taget_theta = calculate_target_theta(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta,4) == round(0.8333333 * math.pi,4)

def test_when_deg_in_forth_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 1.0
    target_y = -math.sqrt(3)
    taget_theta = calculate_target_theta(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta,4) == round(0.166666667 * math.pi,4)

