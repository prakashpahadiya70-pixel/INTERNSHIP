import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load Dataset
df = pd.read_csv("house_data.csv")

# Features and Target
X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
joblib.dump(model, "house_price_model.pkl")

print("✅ House Price Model Trained Successfully!")
print("✅ Model saved as house_price_model.pkl")