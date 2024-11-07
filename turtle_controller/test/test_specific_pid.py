import math
from turtle_controller.utils.specific_pid import MovmentPid


def test_when_try_to_get_from_zero_zero_to_bigger_than_max_error_then_returns_half_p_multiple_by_sqrt2():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, 0
    current_theta = 0
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == 0


def test_when_in_0_0_and_theta_0_and_try_to_go_to_first_quarter_then_angular_is_p_z_relative_pi_and_linear_p_x():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, 5
    current_theta = 0
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == p_z / 4


def test_when_in_0_0_and_theta_0_and_try_to_go_to_second_quarter_then_angular_is_p_z_relative_pi_and_linear_p_x():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = -5, 5
    current_theta = 0
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == (3 / 4) * p_z


def test_when_in_0_0_and_theta_0_and_try_to_go_to_third_quarter_then_angular_is_p_z_relative_pi_and_linear_p_x():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = -5, -5
    current_theta = 0
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == -(3 / 4) * p_z


def test_when_in_0_0_and_theta_0_and_try_to_go_to_forth_quarter_then_angular_is_p_z_relative_pi_and_linear_p_x():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, -5
    current_theta = 0
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == -(1 / 4) * p_z
