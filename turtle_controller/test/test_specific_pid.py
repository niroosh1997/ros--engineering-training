import math
from turtle_controller.utils.specific_pid import MovmentPid


def test_when_try_to_get_from_zero_zero_to_bigger_than_max_error_then_returns_half_p_multiple_by_sqrt2():
    p_x = 2
    p_z = 2
    movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
    current_x, current_y = 0, 0
    target_x, target_y = 5, 0
    current_theta = math.pi * 0.5
    linear_x, angular_z = movement_pid.go_to(
        current_x, current_y, current_theta, target_x, target_y
    )
    assert linear_x == p_x
    assert angular_z == 0


# def test_when_try_to_get_from_zero_zero_to_bigger_than_max_error_then_returns_half_p_multiple_by_sqrt2():
#     p_x = 2
#     p_z = 2
#     movement_pid = MovmentPid(p_x=p_x, p_z=p_z, max_error=1)
#     current_x, current_y = 0, 0
#     target_x, target_y = 5, 5
#     current_theta = math.pi * 0.5
#     linear_x, angular_z = movement_pid.go_to(
#         current_x, current_y, current_theta, target_x, target_y
#     )
#     assert linear_x == p_x
#     assert angular_z == p_z


# def test_when_try_to_get_from_zero_zero_to_half_max_error_than_returns_quarter_p_multiple_by_sqrt2():
#     p = 2
#     movement_pid = MovmentPid(p=p, max_error=14.142135624)
#     current_x, current_y = 0, 0
#     target_x, target_y = 5, 5
#     linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
#     assert round(linear_x, 3) == round((p / 4) * math.sqrt(2), 3)
#     assert round(linear_y, 3) == round((p / 4) * math.sqrt(2), 3)


# def test_try_to_get_from_zero_zero_to_second_quarter():
#     p = 2
#     movement_pid = MovmentPid(p=p, max_error=1)
#     current_x, current_y = 0, 0
#     target_x, target_y = -5, 5
#     linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
#     assert round(linear_x, 3) == round(-(p / 2) * math.sqrt(2), 3)
#     assert round(linear_y, 3) == round((p / 2) * math.sqrt(2), 3)


# def test_try_to_get_from_zero_zero_to_third_quarter():
#     p = 2
#     movement_pid = MovmentPid(p=p, max_error=1)
#     current_x, current_y = 0, 0
#     target_x, target_y = -5, -5
#     linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
#     assert round(linear_x, 3) == round(-(p / 2) * math.sqrt(2), 3)
#     assert round(linear_y, 3) == round(-(p / 2) * math.sqrt(2), 3)


# def test_try_to_get_from_zero_zero_to_forth_quarter():
#     p = 2
#     movement_pid = MovmentPid(p=p, max_error=1)
#     current_x, current_y = 0, 0
#     target_x, target_y = 5, -5
#     linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
#     assert round(linear_x, 3) == round((p / 2) * math.sqrt(2), 3)
#     assert round(linear_y, 3) == round(-(p / 2) * math.sqrt(2), 3)


# def test_try_to_get_from_zero_zero_to_down():
#     p = 2
#     movement_pid = MovmentPid(p=p, max_error=1)
#     current_x, current_y = 0, 0
#     target_x, target_y = 0, -5
#     linear_x, linear_y = movement_pid.go_to(current_x, current_y, target_x, target_y)
#     assert round(linear_x, 3) == round(0)
#     assert round(linear_y, 3) == round(-2, 3)  # need to check
