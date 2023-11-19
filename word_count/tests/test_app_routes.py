import json
from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_read_healthz() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Healthy!!!"


def test_words_count_4() -> None:
    response = client.post(
        "/count",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"text": "the weather is good"}),
    )
    assert response.status_code == 200
    assert response.json()["result"] == 4


def test_words_count_2() -> None:
    response = client.post(
        "/count",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"text": "the weather "}),
    )
    assert response.status_code == 200
    assert response.json()["result"] == 2
