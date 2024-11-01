import math

from turtle_controller.utils.direction_calculation import calculate_target_theta_of_velocity
from turtle_controller.utils.pid import Pid


class MovmentPid:
    def __init__(
        self, p: float, i: float = 0, sample_time: float = 1, max_error: float = 1
    ) -> None:
        self._pid_x = Pid(p=p, i=i, sample_time=sample_time)
        self._pid_y = Pid(p=p, i=i, sample_time=sample_time)
        self._max_error = max_error

    def go_to(self, current_x: float, current_y: float, target_x: float, target_y: float):
        direction_theta = calculate_target_theta_of_velocity(
            current_x, current_y, target_x, target_y
        )
        direction_x, direction_y = math.cos(direction_theta), math.sin(direction_theta)
        error_x = (target_x - current_x) / self._max_error
        error_y = (target_y - current_y) / self._max_error
        return (
            direction_x * abs(self._pid_x.calculate_output(error_x)),
            direction_y * abs(self._pid_y.calculate_output(error_y)),
        )
