class Pid:
    def __init__(self, p: float) -> None:
        self._p = p

    def calculate_output(self, error: float):
        error = min(error, 1)
        error = max(error, -1)
        output_pid = 0
        output_pid += error * self._p
        return output_pid
