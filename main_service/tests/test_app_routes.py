import json
from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_read_docs() -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_read_healthz() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Healthy!!!"


def test_list_services() -> None:
    response = client.get("/services")
    assert response.status_code == 200
    assert response.json() == []


def test_register_service() -> None:
    response = client.post(
        "/services",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"name": "sentiment-analysis", "url": "http://localhost:8001/analyze"}),
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Service registered successfully"

    response = client.post(
        "/services",
        headers={"Content-Type": "application/json"},
        content=json.dumps({"name": "sentiment-analysis", "url": "http://localhost:8002/analyze"}),
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Service already registered"


def test_delete_service() -> None:
    service_name = "sentiment-analysis"
    response = client.delete(f"/services/{service_name}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Service {service_name} deleted successfully"
    response = client.delete(f"/services/{service_name}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Service {service_name} not found"
