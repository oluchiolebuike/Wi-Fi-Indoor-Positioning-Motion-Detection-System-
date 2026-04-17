import joblib
import numpy as np

model = joblib.load("ml/position_model.pkl")

def predict_position(rssi_vector):
    pred = model.predict([rssi_vector])
    return pred[0]