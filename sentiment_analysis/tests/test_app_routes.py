import json
from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_read_healthz() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Healthy!!!"


def test_analyze() -> None:
    response = client.post(
        "/analyze",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"text": "the weather is good"}),
    )
    assert response.status_code == 200
    assert response.json()["result"] == "positive"


def test_analyze_negative() -> None:
    response = client.post(
        "/analyze",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"text": "the weather is bad!"}),
    )
    assert response.status_code == 200
    assert response.json()["result"] == "negative"
