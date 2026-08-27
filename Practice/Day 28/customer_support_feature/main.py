from response_handler import get_customer_response


def run_customer_support():
    """Run the customer support application."""
    print("=" * 50)
    print("       AI CUSTOMER SUPPORT")
    print("=" * 50)

    customer_message = input("Enter your question: ")

    response = get_customer_response(customer_message)

    print("\nSupport Response:")
    print(response)


if __name__ == "__main__":
    run_customer_support()