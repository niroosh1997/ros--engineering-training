import math

def calculate_target_theta(current_x: float, current_y: float, target_x: float, target_y: float):
    if target_y >= 0:
        return 0.75 * math.pi
    if target_y < 0:
        return 0.25 * math.pi 