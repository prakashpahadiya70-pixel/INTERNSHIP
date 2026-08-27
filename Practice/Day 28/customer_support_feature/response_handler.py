SUPPORT_RESPONSES = {
    "refund": "Your refund request has been received. Our team will process it soon.",
    "order": "Please provide your order ID so we can check your order status.",
    "password": "You can reset your password using the Forgot Password option.",
    "greeting": "Hello! How can I help you today?"
}


def get_customer_response(message):
    """
    Generate a customer support response based on the customer's message.

    Args:
        message (str): Customer's support question.

    Returns:
        str: Appropriate support response.
    """
    if not message or not message.strip():
        return "Please enter a valid customer question."

    message = message.lower().strip()

    if "refund" in message:
        return SUPPORT_RESPONSES["refund"]

    if "order" in message:
        return SUPPORT_RESPONSES["order"]

    if "password" in message:
        return SUPPORT_RESPONSES["password"]

    if "hello" in message or "hi" in message:
        return SUPPORT_RESPONSES["greeting"]

    return (
        "Sorry, I could not understand your request. "
        "Please contact customer support."
    )