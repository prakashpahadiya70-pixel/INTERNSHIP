try:
    from flask import Flask, jsonify, request
except ImportError as e:
    raise ImportError("Flask is not installed. Install it with 'pip install flask'.") from e

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Rahul",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "Priya",
        "department": "HR"
    }
]

# Hello World API
@app.route("/")
def home():
    return jsonify({
        "message": "Hello World API is Running"
    })

# GET API
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# POST API
@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.json

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"]
    }

    employees.append(new_employee)

    return jsonify({
        "message": "Employee Added Successfully",
        "employee": new_employee
    }), 201

# PUT API
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    data = request.json

    for employee in employees:

        if employee["id"] == id:

            employee["name"] = data["name"]
            employee["department"] = data["department"]

            return jsonify({
                "message": "Employee Updated Successfully",
                "employee": employee
            })

    return jsonify({
        "message": "Employee Not Found"
    }), 404

# DELETE API
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    for employee in employees:

        if employee["id"] == id:

            employees.remove(employee)

            return jsonify({
                "message": "Employee Deleted Successfully"
            })

    return jsonify({
        "message": "Employee Not Found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)