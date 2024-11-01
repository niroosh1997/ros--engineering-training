import math

def calculate_target_theta(current_x: float, current_y: float, target_x: float, target_y: float):
    tan_target = target_y / target_x
    x_axis_angle = 0.5 * math.pi
    if target_x >= 0:
        return x_axis_angle + math.atan(tan_target) 
    if target_x < 0:
        return (-x_axis_angle + math.atan(tan_target))