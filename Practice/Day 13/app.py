from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("employee_model.pkl")

@app.route("/")
def home():
    return "Employee Prediction API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Check JSON
        if data is None:
            return jsonify({"error": "No JSON received"}), 400

        # Check salary field
        if "salary" not in data:
            return jsonify({"error": "Salary field missing"}), 400

        salary = data["salary"]

        # Check data type
        if not isinstance(salary, (int, float)):
            return jsonify({"error": "Salary must be a number"}), 400

        # Check negative value
        if salary < 0:
            return jsonify({"error": "Salary cannot be negative"}), 400

        # Prediction
        prediction = model.predict([[salary]])

        return jsonify({
            "prediction": prediction[0]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)