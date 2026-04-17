## WiFi Indoor Positioning Motion Detection System

## Overview

This project is a Wi-Fi-based indoor positioning and motion detection system.
It uses RSSI (signal strength) and CSI (signal structure) combined with machine learning
to estimate indoor position and detect motion without GPS, cameras or wearables.


## Features

- Indoor positioning using Wi-Fi RSSI fingerprinting
- Motion detection using CSI signal analysis
- Machine learning models (k-NN, SVM)
- Signal processing (FFT, Kalman filter, noise reduction)
- MQTT-based real-time data streaming
- ESP32 + Raspberry Pi integration
- FastAPI backend for live data access


## How it works

1. ESP32 collects Wi-Fi RSSI and CSI signals
2. Data is sent via MQTT
3. Python backend receives real-time data
4. Machine learning models predict:
   - Indoor position (x, y)
   - Motion state (stationary, walking, running)
5. Results are exposed via API


## Machine Learning Models

POSITION MODEL:
- Algorithm: k-NN
- Input: RSSI values
- Output: (x, y) coordinates

MOTION MODEL:
- Algorithm: SVM
- Input: CSI features (mean, variance, FFT energy)
- Output: motion class


## Signal Processing

- Hampel filter: removes RSSI outliers
- Kalman filter: smooths position estimates
- FFT: extracts frequency patterns from CSI signals

## Installation


### Install dependencies:

pip install numpy pandas scikit-learn paho-mqtt fastapi uvicorn joblib

### Install MQTT broker (Mosquitto):

### Ubuntu:
sudo apt install mosquitto mosquitto-clients

### Windows:
Download Mosquitto from official site


## How to run the system


### STEP 1: Start MQTT Broker

mosquitto

or on Raspberry Pi:
sudo systemctl start mosquitto


### STEP 2: Start MQTT Subscriber

python mqtt/subscriber.py


### STEP 3: Start Main ML Engine

python main.py


### STEP 4: Start API Server

uvicorn backend.api:app --reload

API will be available at:
http://127.0.0.1:8000


### DATA FORMAT

#### RSSI INPUT EXAMPLE:

ap1, ap2, ap3
-45, -60, -70

#### Output:
(x, y) position coordinates


### MOTION INPUT FEATURES:

mean, variance, fft_energy

#### Output:
stationary / walking / running



## Future Improvements

- Deep learning models (CNN / LSTM)
- Particle filter localization
- Multi-floor tracking
- React live dashboard
- Cloud MQTT integration (AWS IoT Core)
- Mobile app integration


## License
This project is for educational and research purposes only.
