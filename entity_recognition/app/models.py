from pydantic import BaseModel


class AnalyzeRequestModel(BaseModel):
    text: str


class EntityLabel(BaseModel):
    entity: str
    label: str


class AnalyzeResponseModel(BaseModel):
    result: list[EntityLabel]
