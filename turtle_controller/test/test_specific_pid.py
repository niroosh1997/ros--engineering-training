from turtle_controller.specific_pid import MovmentPid


def test_when_try_to_get_from_zero_zero_to_bigger_than_max_error_then_returns_sqrt2():
    movement_pid = MovmentPid(p=2, max_error=1)
    current_x = 0
    current_y = 0
    target_x = 5
    target_y = 5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round(1.414, 3)
    assert round(linear_y, 3) == round(1.414, 3)


def test_when_try_to_get_from_zero_zero_to_half_max_error_than_returns_half_sqrt2():
    movement_pid = MovmentPid(p=2, max_error=10)
    current_x = 0
    current_y = 0
    target_x = 5
    target_y = 5
    linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
    assert round(linear_x, 3) == round(0.707, 3)
    assert round(linear_y, 3) == round(0.707, 3)
