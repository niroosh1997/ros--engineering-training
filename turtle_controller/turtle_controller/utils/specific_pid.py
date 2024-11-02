import math

from turtle_controller.utils.direction_calculation import calculate_target_theta_of_velocity
from turtle_controller.utils.pid import Pid


class MovmentPid:
    def __init__(
        self, p: float, i: float = 0, sample_time: float = 1, max_error: float = 1
    ) -> None:
        self._pid = Pid(p=p, i=i, sample_time=sample_time)
        self._max_error = max_error

    def _calculate_distance_error(
        self, current_x: float, current_y: float, target_x: float, target_y: float
    ):
        power_of_delta_x = math.pow((target_x - current_x), 2)
        power_of_delta_y = math.pow((target_y - current_y), 2)
        distance = math.sqrt(power_of_delta_x + power_of_delta_y)
        error = distance / self._max_error
        return error

    def go_to(self, current_x: float, current_y: float, target_x: float, target_y: float):
        direction_theta = calculate_target_theta_of_velocity(
            current_x, current_y, target_x, target_y
        )
        direction_x, direction_y = math.cos(direction_theta), math.sin(direction_theta)
        error = self._calculate_distance_error(current_x, current_y, target_x, target_y)
        calculated_speed_size = abs(self._pid.calculate_output(error))
        return (
            (direction_x * calculated_speed_size),
            (direction_y * calculated_speed_size),
        )
