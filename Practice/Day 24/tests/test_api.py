import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_company_endpoint():
    response = client.get("/company")

    assert response.status_code == 200
    assert response.json()["company"] == "ABC Technologies"


def test_support_endpoint():
    response = client.post(
        "/support",
        json={
            "name": "Himanshu",
            "message": "I need help with my account"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["customer"] == "Himanshu"