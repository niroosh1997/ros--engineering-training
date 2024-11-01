from turtle_controller.pid import pid


def test_when_error_is_zero_then_pid_returns_zero():
    pid(target=5, current=5, p=10)
