import re


def send_email(to, subject, body):
    try:
        # Validate email address
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, to):
            return {
                "success": False,
                "error": "Invalid email address."
            }

        if not subject.strip():
            return {
                "success": False,
                "error": "Email subject cannot be empty."
            }

        if not body.strip():
            return {
                "success": False,
                "error": "Email body cannot be empty."
            }

        # Safe testing mode
        return {
            "success": True,
            "mode": "TEST",
            "message": "Email prepared successfully.",
            "to": to,
            "subject": subject,
            "body": body
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Email Tool Error: {str(e)}"
        }


if __name__ == "__main__":

    print("Email Tool")
    print("=" * 40)

    to = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter email body: ")

    result = send_email(to, subject, body)

    if result["success"]:

        print("\nEmail Preview")
        print("=" * 40)
        print("Mode:", result["mode"])
        print("To:", result["to"])
        print("Subject:", result["subject"])
        print("Body:", result["body"])

    else:
        print("\nError:", result["error"])