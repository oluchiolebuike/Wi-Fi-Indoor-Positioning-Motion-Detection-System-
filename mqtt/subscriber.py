import json
import paho.mqtt.client as mqtt

# store latest RSSI readings
latest_rssi = {}

# when message is received
def on_message(client, userdata, msg):
    global latest_rssi

    data = json.loads(msg.payload.decode())

    # example format:
    # {"ap1": -45, "ap2": -60, "ap3": -70}

    latest_rssi = data
    print("Received RSSI:", latest_rssi)


client = mqtt.Client()

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("wifi/rssi")

client.loop_forever()