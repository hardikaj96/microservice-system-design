import json
import requests

main_service_url = "http://localhost:8000"


def register_service(name, url):
    data = json.dumps({"name": name, "url": url})
    return requests.post(f"{main_service_url}/services", data=data)


def list_services():
    return requests.get(f"{main_service_url}/services")


def delete_service(name):
    return requests.delete(f"{main_service_url}/services/{name}")


def analyze(service, text):
    data = json.dumps({"service": service, "text": text})
    return requests.post(f"{main_service_url}/analyze", data=data)


# def test_list_services():
#     response = list_services()

#     assert response.status_code == 200
#     assert response.json() == []


def test_register_services():
    name = "sentiment_analysis"
    url = "http://host.docker.internal:8001/analyze"
    response = register_service(name, url)
    assert response.status_code == 201
    assert response.json() == {"message": "Service registered successfully"}


def test_delete_service():
    response = delete_service("sentiment_analysis")
    assert response.status_code == 200


def test_multiple_services():
    name1 = "sentiment_analysis"
    url1 = "http://host.docker.internal:8001/analyze"
    name2 = "word_count"
    url2 = "http://host.docker.internal:8002/count"
    name3 = "entity_recognition"
    url3 = "http://host.docker.internal:8003/recognize"

    _ = register_service(name1, url1)
    _ = register_service(name2, url2)
    _ = register_service(name3, url3)

    response = list_services()

    assert response.status_code == 200
    assert response.json() == [
        {"name": name1, "url": url1},
        {"name": name2, "url": url2},
        {"name": name3, "url": url3},
    ]

    _ = delete_service(name1)
    _ = delete_service(name2)
    _ = delete_service(name3)


def test_existing_service():
    name1 = "sentiment_analysis"
    url1 = "http://host.docker.internal:8001/analyze"
    _ = register_service(name1, url1)
    data = json.dumps({"service": name1, "text": "The weather is great"})
    response = requests.post(f"{main_service_url}/analyze", data=data)
    assert response.status_code == 200
    assert response.json() == {"result": "Positive"}
    _ = delete_service(name1)


def test_non_existing_service():
    data = json.dumps({"service": "text_analysis", "text": "The weather is great"})
    response = requests.post(f"{main_service_url}/analyze", data=data)
    assert response.status_code == 404
    assert response.json() == {"detail": {"error": "Requested service does not exist"}}


def test_sentiment_analysis_service():
    name = "sentiment_analysis"
    url = "http://host.docker.internal:8001/analyze"
    _ = register_service(name, url)
    data = json.dumps({"service": name, "text": "The weather is great"})
    response = requests.post(f"{main_service_url}/analyze", data=data)
    assert response.status_code == 200
    assert response.json() == {"result": "Positive"}
    _ = delete_service(name)


def test_word_count_service():
    name = "word_count"
    url = "http://host.docker.internal:8002/count"
    _ = register_service(name, url)
    data = json.dumps({"service": name, "text": "The weather is great"})
    response = requests.post(f"{main_service_url}/analyze", data=data)
    assert response.status_code == 200
    assert response.json() == {"result": 4}
    _ = delete_service(name)


def test_entity_recognition_service():
    name = "entity_recognition"
    url = "http://host.docker.internal:8003/recognize"
    _ = delete_service(name)

    _ = register_service(name, url)
    data = json.dumps({"service": name, "text": "The weather is great"})
    response = requests.post(f"{main_service_url}/analyze", data=data)
    assert response.status_code == 200
    assert response.json() == {"result": []}
    _ = delete_service(name)
