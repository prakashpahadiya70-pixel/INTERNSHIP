from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")

@app.route("/")
def home():
    return "House Price Prediction API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"error": "No JSON data received"}), 400

        required_fields = ["area", "bedrooms", "bathrooms"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is missing"}), 400

        area = data["area"]
        bedrooms = data["bedrooms"]
        bathrooms = data["bathrooms"]

        if not isinstance(area, (int, float)):
            return jsonify({"error": "Area must be a number"}), 400

        if not isinstance(bedrooms, int):
            return jsonify({"error": "Bedrooms must be an integer"}), 400

        if not isinstance(bathrooms, int):
            return jsonify({"error": "Bathrooms must be an integer"}), 400

        if area <= 0 or bedrooms <= 0 or bathrooms <= 0:
            return jsonify({"error": "Values must be greater than zero"}), 400

        prediction = model.predict([[area, bedrooms, bathrooms]])

        return jsonify({
            "predicted_price": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)