import joblib

model = joblib.load("ml/motion_model.pkl")

def predict_motion(features):
    return model.predict([features])[0]