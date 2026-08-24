def calculator(operation, a, b):
    try:
        if operation == "add":
            return a + b

        elif operation == "subtract":
            return a - b

        elif operation == "multiply":
            return a * b

        elif operation == "divide":
            if b == 0:
                return "Error: Cannot divide by zero."
            return a / b

        else:
            return "Error: Invalid operation."

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("Calculator Tool")
    print("----------------")

    print("Addition:", calculator("add", 10, 5))
    print("Subtraction:", calculator("subtract", 10, 5))
    print("Multiplication:", calculator("multiply", 10, 5))
    print("Division:", calculator("divide", 10, 5))
    print("Error Test:", calculator("divide", 10, 0))