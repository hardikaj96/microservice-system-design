import json

import requests
from app.models import ServiceModel


class ServiceRegister:
    def __init__(self):
        self.services: list[ServiceModel] = []

    def get_service_url(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service.url
        return None

    def perform_service_request(self, service_url, text):
        try:
            data = json.dumps({"text": text})
            response = requests.post(service_url, data=data)
            return response.json()
        except requests.exceptions.RequestException:
            return None
