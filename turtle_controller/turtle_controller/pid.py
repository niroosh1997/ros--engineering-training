def pid(target: float, current: float, max_error: float, p: float):
    error = target - current
    output_pid = error / max_error
    output_pid = min(output_pid, 1)
    output_pid = max(output_pid, -1)
    return output_pid * p
