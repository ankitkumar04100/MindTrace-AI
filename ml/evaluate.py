import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

# Load data
data = pd.read_csv("data/sample_dataset.csv")
X = data[["response_time", "error_rate", "consistency", "fatigue_index"]]
y = data["stress_label"]

# Load trained model
model = joblib.load("model/stress_model.pkl")

# Predict
predictions = model.predict(X)

# Metrics
accuracy = accuracy_score(y, predictions)
report = classification_report(y, predictions)

print("📊 Model Evaluation Results")
print("Accuracy:", round(accuracy, 2))
print("\nClassification Report:\n", report)
