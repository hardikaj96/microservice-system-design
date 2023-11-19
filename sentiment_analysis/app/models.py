from pydantic import BaseModel


class AnalyzeRequestModel(BaseModel):
    text: str


class AnalyzeResponseModel(BaseModel):
    result: str
