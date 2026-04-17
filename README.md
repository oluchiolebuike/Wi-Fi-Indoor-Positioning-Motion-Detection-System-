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

pip install numpy pandas scikit-learn paho-mqtt fastapi uvicorn joblib

MQTT Broker:
Install Mosquitto


## Running the project 

### Start MQTT subscriber:
python mqtt/subscriber.py

### Run main system:
python main.py

### Start API server:
uvicorn backend.api:app --reload


## Future Improvements

- Deep learning models (CNN / LSTM)
- Particle filter localization
- Multi-floor tracking
- React live dashboard
- Cloud MQTT integration (AWS IoT Core)
- Mobile app integration


## License
This project is for educational and research purposes only.
