from pydantic import BaseModel


class CountRequestModel(BaseModel):
    text: str


class CountResponseModel(BaseModel):
    result: int
