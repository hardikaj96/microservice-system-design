from fastapi import APIRouter, Body, status
from app.models import CountRequestModel, CountResponseModel
from app.services import count_words

router = APIRouter(
    include_in_schema=True,
)


@router.get("/health")
def healthz():
    return {"status": "Healthy!!!"}


@router.post("/count", response_model=CountResponseModel)
async def wordcount(req: CountRequestModel = Body(...)):
    return {"result": count_words(req.text)}
