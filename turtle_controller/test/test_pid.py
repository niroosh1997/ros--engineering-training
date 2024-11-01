from turtle_controller.pid import pid


def test_when_error_is_zero_then_pid_returns_zero():
    assert pid(target=5, current=5, max_error=20, p=10) == 0


def test_when_error_bigger_than_max_error_then_pid_returns_p():
    p = 10
    assert pid(target=7, current=5, max_error=2, p=p) == p


def test_when_error_half_of_max_error_then_pid_returns_half_p():
    p = 10
    assert pid(target=6, current=5, max_error=2, p=p) == p / 2
