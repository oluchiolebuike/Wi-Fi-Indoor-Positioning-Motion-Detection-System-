import numpy as np

previous_rssi = None

def detect_motion(current_rssi):
    global previous_rssi

    if previous_rssi is None:
        previous_rssi = current_rssi
        return "stationary"

    diff = []

    for ap in current_rssi:
        if ap in previous_rssi:
            diff.append(abs(current_rssi[ap] - previous_rssi[ap]))

    previous_rssi = current_rssi

    avg_change = np.mean(diff) if diff else 0

    if avg_change < 2:
        return "stationary"
    elif avg_change < 6:
        return "walking"
    else:
        return "moving"