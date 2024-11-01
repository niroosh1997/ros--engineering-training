def pid(target: float, current: float, max_error: float, p: float):
    error = target - current
    output_pid = error / max_error
    if output_pid >= 1:
        return p
    if output_pid <= -1:
        return -p
    return output_pid * p
