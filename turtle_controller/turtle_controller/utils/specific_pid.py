import math

from turtle_controller.utils.direction_calculation import calculate_target_theta_of_angular
from turtle_controller.utils.pid import Pid


class MovmentPid:
    def __init__(
        self, p_x: float, p_z: float, i: float = 0, sample_time: float = 1, max_error: float = 1
    ) -> None:
        self._distance_pid = Pid(p=p_x, i=i, sample_time=sample_time)
        self._angular_pid = Pid(p=p_z, i=i, sample_time=sample_time)
        self._max_error = max_error

    def _calculate_distance_error(
        self, current_x: float, current_y: float, target_x: float, target_y: float
    ):
        power_of_delta_x = math.pow((target_x - current_x), 2)
        power_of_delta_y = math.pow((target_y - current_y), 2)
        distance = math.sqrt(power_of_delta_x + power_of_delta_y)
        error = distance / self._max_error
        return error

    def go_to(
        self,
        current_x: float,
        current_y: float,
        current_theta: float,
        target_x: float,
        target_y: float,
    ):
        direction_theta = calculate_target_theta_of_angular(
            current_x, current_y, target_x, target_y
        )
        print(f"{current_x} {current_y} {current_theta} {target_x} {target_y} {direction_theta}")
        error_distance = self._calculate_distance_error(current_x, current_y, target_x, target_y)
        error_angular = (direction_theta - current_theta) / math.pi * 2
        calculated_speed_size = abs(self._distance_pid.calculate_output(error_distance))
        calculated_angular_speed_size = abs(self._angular_pid.calculate_output(error_angular))
        return calculated_speed_size, calculated_angular_speed_size
