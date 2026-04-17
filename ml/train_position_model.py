import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

# load dataset
# columns: ap1, ap2, ap3, x, y
data = pd.read_csv("data/fingerprint_dataset.csv")

X = data[["ap1", "ap2", "ap3"]]
y = data[["x", "y"]]

# k-NN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# save model
joblib.dump(model, "ml/position_model.pkl")

print("Position model trained and saved.")