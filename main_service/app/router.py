from fastapi import APIRouter, Body, HTTPException, status
from app.models import AnalyzeRequestModel, ServiceModel, ServiceAddResponseModel
from app.services import ServiceRegister

router = APIRouter(
    include_in_schema=True,
)

register = ServiceRegister()


@router.get("/health")
def healthz():
    return {"status": "Healthy!!!"}


@router.post(
    "/services", response_model=ServiceAddResponseModel, status_code=status.HTTP_201_CREATED
)
async def register_service(service: ServiceModel = Body(...)):
    # Check if the service is already registered
    if any(s.name == service.name for s in register.services):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Service already registered"
        )

    register.services.append(service)

    return {"message": "Service registered successfully"}


@router.get("/services", response_model=list[ServiceModel])
async def list_services():
    return register.services


@router.delete("/services/{service_name}", response_model=dict)
async def delete_service(service_name: str):
    for service in register.services:
        if service.name == service_name:
            register.services.remove(service)
            return {"message": f"Service {service_name} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Service {service_name} not found")


@router.post("/analyze", response_model=dict)
async def analyze_text(request: AnalyzeRequestModel = Body(...)):
    service_url = register.get_service_url(request.service)
    if not service_url:
        raise HTTPException(status_code=404, detail={"error": "Requested service does not exist"})
    results = register.perform_service_request(service_url, request.text)
    if not results:
        raise HTTPException(status_code=404, detail={"error": "No result from requested service"})
    return results
