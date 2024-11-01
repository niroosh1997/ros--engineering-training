import math

from turtle_controller.direction_calculation import (
    calculate_target_theta_of_angular,
    calculate_target_theta_of_velocity,
)


def test_when_deg_in_first_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 1
    target_y = math.sqrt(3)
    taget_theta = calculate_target_theta_of_angular(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(0.8333333 * math.pi, 4)


def test_when_deg_in_forth_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 1.0
    target_y = -math.sqrt(3)
    taget_theta = calculate_target_theta_of_angular(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(0.166666667 * math.pi, 4)


def test_when_deg_in_second_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = -1.0
    target_y = math.sqrt(3)
    taget_theta = calculate_target_theta_of_angular(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(-0.8333333 * math.pi, 4)


def test_when_deg_in_third_square_then_taget_theta_is_like_calculation():
    currect_x = 0.0
    currect_y = 0.0
    target_x = -1.0
    target_y = -math.sqrt(3)
    taget_theta = calculate_target_theta_of_angular(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(-0.166666667 * math.pi, 4)


def test_when_current_not_0_0_then_use_delta_in_positions_in_calculations():
    currect_x = -1
    currect_y = -math.sqrt(3)
    target_x = 0
    target_y = 0
    taget_theta = calculate_target_theta_of_angular(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(0.8333333 * math.pi, 4)


def test_when_calculate_velocity_theta_in_first_square_then_output_accordingly():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 1
    target_y = math.sqrt(3)
    taget_theta = calculate_target_theta_of_velocity(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(0.3333333 * math.pi, 4)


def test_when_calculate_velocity_theta_in_with_delta_x_zero_then_returns_pi_divide_by_4():
    currect_x = 0.0
    currect_y = 0.0
    target_x = 0.0
    target_y = math.sqrt(3)
    taget_theta = calculate_target_theta_of_velocity(currect_x, currect_y, target_x, target_y)
    assert round(taget_theta, 4) == round(0.25 * math.pi, 4)
