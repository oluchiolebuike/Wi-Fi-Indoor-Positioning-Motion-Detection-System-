from mqtt.subscriber import latest_rssi
from inference.predict_position import predict_position
from inference.predict_motion import predict_motion
import time

while True:
    if latest_rssi:

        # POSITION ML
        rssi_vector = [
            latest_rssi.get("ap1", -100),
            latest_rssi.get("ap2", -100),
            latest_rssi.get("ap3", -100)
        ]

        position = predict_position(rssi_vector)

        # MOTION ML (placeholder features for now)
        motion_features = [10, 2, 0.5]  # replace with CSI extraction later
        motion = predict_motion(motion_features)

        print("Position:", position)
        print("Motion:", motion)

    time.sleep(1)