from pydantic import BaseModel


class ServiceModel(BaseModel):
    name: str
    url: str


class ServiceAddResponseModel(BaseModel):
    message: str


class AnalyzeRequestModel(BaseModel):
    service: str
    text: str
