import math

# fake AP coordinates
ACCESS_POINTS = {
    "ap1": (0, 0),
    "ap2": (10, 0),
    "ap3": (5, 10)
}

def rssi_to_distance(rssi):
    # vERY simplified model (expand later)
    return 10 ** ((-50 - rssi) / 20)


def estimate_position(rssi_data):
    x_sum, y_sum, weight_sum = 0, 0, 0

    for ap, rssi in rssi_data.items():
        if ap not in ACCESS_POINTS:
            continue

        x, y = ACCESS_POINTS[ap]
        distance = rssi_to_distance(rssi)

        weight = 1 / (distance + 0.001)

        x_sum += x * weight
        y_sum += y * weight
        weight_sum += weight

    if weight_sum == 0:
        return (0, 0)

    return (x_sum / weight_sum, y_sum / weight_sum)