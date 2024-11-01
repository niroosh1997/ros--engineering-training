import math
from turtle_controller.specific_pid import MovmentPid


def test_when_try_to_get_from_zero_zero_to_bigger_than_max_error_then_returns_half_p_multiple_by_sqrt2():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, 5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round((p / 2) * math.sqrt(2), 3)
    assert round(linear_y, 3) == round((p / 2) * math.sqrt(2), 3)


def test_when_try_to_get_from_zero_zero_to_half_max_error_than_returns_quarter_p_multiple_by_sqrt2():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=10)
    current_x, current_y = 0, 0
    target_x, target_y = 5, 5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round((p / 4) * math.sqrt(2), 3)
    assert round(linear_y, 3) == round((p / 4) * math.sqrt(2), 3)


def test_try_to_get_from_zero_zero_to_second_quarter():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = -5, 5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round(-(p / 2) * math.sqrt(2), 3)
    assert round(linear_y, 3) == round((p / 2) * math.sqrt(2), 3)


def test_try_to_get_from_zero_zero_to_third_quarter():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = -5, -5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round(-(p / 2) * math.sqrt(2), 3)
    assert round(linear_y, 3) == round(-(p / 2) * math.sqrt(2), 3)


def test_try_to_get_from_zero_zero_to_forth_quarter():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, -5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round((p / 2) * math.sqrt(2), 3)
    assert round(linear_y, 3) == round(-(p / 2) * math.sqrt(2), 3)


def test_try_to_get_from_zero_zero_to_down():
    p = 2
    movement_pid = MovmentPid(p=p, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 0, -5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round(0)
    assert round(linear_y, 3) == round(-(p / 2) * math.sqrt(2), 3)  # need to check
