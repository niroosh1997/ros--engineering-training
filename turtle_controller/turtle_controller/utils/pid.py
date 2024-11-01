class Pid:
    def __init__(self, p: float, i: float = 0, sample_time: float = 1) -> None:
        self._p = p
        self._i = i
        self._sample_time = sample_time
        self._prev_error = 0

    def calculate_output(self, error: float) -> float:
        error = self._range_between_1_and_minus_1(error)
        output_pid = 0
        output_pid += error * self._p
        output_pid += self._i * (error - self._prev_error) * self._sample_time / 2
        return output_pid

    def _range_between_1_and_minus_1(self, error: float) -> float:
        error = min(error, 1)
        error = max(error, -1)
        return error
