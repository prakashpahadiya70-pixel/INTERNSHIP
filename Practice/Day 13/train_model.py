import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample dataset
data = {
    "salary": [15000, 18000, 25000, 30000, 35000, 45000, 50000, 60000, 70000, 85000],
    "position": [
        "Junior Employee",
        "Junior Employee",
        "Junior Employee",
        "Mid Employee",
        "Mid Employee",
        "Senior Employee",
        "Senior Employee",
        "Senior Employee",
        "Manager",
        "Manager"
    ]
}

# DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["salary"]]
y = df["position"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save Model
joblib.dump(model, "employee_model.pkl")

print("✅ Model saved successfully as employee_model.pkl")