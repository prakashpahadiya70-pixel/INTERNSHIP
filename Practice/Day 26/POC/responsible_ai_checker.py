# Responsible AI Checker - Day 26
# Internship Mini Practical

def check_bias(text):
    bias_keywords = [
        "women are not suitable",
        "men are better",
        "old people cannot",
        "young people are better",
        "disabled people cannot",
        "poor people are",
        "certain race is",
        "certain religion is"
    ]

    text_lower = text.lower()

    for keyword in bias_keywords:
        if keyword in text_lower:
            return "HIGH"

    return "LOW"


def check_privacy(text):
    privacy_keywords = [
        "password",
        "credit card",
        "phone number",
        "email address",
        "aadhaar",
        "pan number",
        "bank account",
        "personal information"
    ]

    text_lower = text.lower()

    for keyword in privacy_keywords:
        if keyword in text_lower:
            return "HIGH"

    return "LOW"


def check_hallucination(text):
    uncertainty_keywords = [
        "i am not sure",
        "may be incorrect",
        "cannot verify",
        "unverified",
        "probably",
        "might be"
    ]

    text_lower = text.lower()

    for keyword in uncertainty_keywords:
        if keyword in text_lower:
            return "MEDIUM"

    return "LOW"


def responsible_ai_check(text):
    bias = check_bias(text)
    privacy = check_privacy(text)
    hallucination = check_hallucination(text)

    risks = [bias, privacy, hallucination]

    if "HIGH" in risks:
        overall = "HIGH"
    elif "MEDIUM" in risks:
        overall = "MEDIUM"
    else:
        overall = "LOW"

    print("\n========================================")
    print("       RESPONSIBLE AI CHECKER")
    print("========================================")

    print(f"Bias Risk          : {bias}")
    print(f"Privacy Risk       : {privacy}")
    print(f"Hallucination Risk : {hallucination}")
    print(f"Overall Risk       : {overall}")

    print("----------------------------------------")

    if overall == "HIGH":
        print("Recommendation: Human review required.")
        print("Do not use this output directly.")
    elif overall == "MEDIUM":
        print("Recommendation: Verify the information before use.")
    else:
        print("Recommendation: No major risk detected.")

    print("========================================")


# Test the Responsible AI Checker
if __name__ == "__main__":

    user_text = input("\nEnter an AI response to check: ")

    responsible_ai_check(user_text)