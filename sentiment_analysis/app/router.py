from fastapi import APIRouter, Body, HTTPException, status
from app.models import AnalyzeRequestModel, AnalyzeResponseModel
from app.services import analyze_sentiment

router = APIRouter(
    include_in_schema=True,
)


@router.get("/health")
def healthz():
    return {"status": "Healthy!!!"}


@router.post("/analyze", response_model=AnalyzeResponseModel)
async def analyze(req: AnalyzeRequestModel = Body(...)):
    return {"result": analyze_sentiment(req.text)}
