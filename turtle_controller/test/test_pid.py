from turtle_controller.pid import Pid


def test_when_error_is_zero_then_pid_returns_zero():
    pid = Pid(p=10)
    assert pid.calculate_output(0) == 0


def test_when_error_bigger_than_one_then_pid_returns_p():
    pid = Pid(p=2)
    assert pid.calculate_output(5) == 2


def test_when_error_leser_than_negative_max_error_then_pid_returns_minus_p():
    pid = Pid(p=2)
    assert pid.calculate_output(-15) == -2


def test_when_error_half_then_pid_returns_half_p():
    pid = Pid(p=2)
    assert pid.calculate_output(0.5) == 1


def test_when_i_is_1_and_error_is_1_then_do_half_error():
    p = 2
    i = 5
    result = 4.5
    pid = Pid(p=p, i=i)
    assert pid.calculate_output(1) == result


def test_when_i_is_1_and_error_is_1_and_sample_is_0_5_then_do_half_error():
    p = 2
    i = 5
    result = 3.25
    pid = Pid(p=p, i=i, sample_time=0.5)
    assert pid.calculate_output(1) == result
