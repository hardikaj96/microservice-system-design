from fastapi import APIRouter, Body
from app.models import AnalyzeRequestModel, AnalyzeResponseModel
from app.services import recognize_entities

router = APIRouter()


@router.get("/health")
def healthz():
    return {"status": "Healthy!!!"}


@router.post("/recognize", response_model=AnalyzeResponseModel)
async def entity_recognition(req: AnalyzeRequestModel = Body(...)):
    return {"result": recognize_entities(req.text)}
