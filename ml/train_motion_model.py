import pandas as pd
from sklearn.svm import SVC
import joblib

# columns: mean, variance, fft_energy, label
data = pd.read_csv("data/csi_dataset.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = SVC(kernel="rbf")
model.fit(X, y)

joblib.dump(model, "ml/motion_model.pkl")

print("Motion model trained.")