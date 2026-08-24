import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import SupportRequest


def test_support_request_model():
    request = SupportRequest(
        name="Himanshu",
        message="I need help with my account"
    )

    assert request.name == "Himanshu"
    assert request.message == "I need help with my account"


def test_support_request_name():
    request = SupportRequest(
        name="Test User",
        message="Test message"
    )

    assert request.name == "Test User"