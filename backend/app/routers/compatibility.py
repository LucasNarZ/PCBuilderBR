from app.schemas import BuildComponents
from app.schemas.build import BuildValidation
from app.services.compatibility import CompatibilityService
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/compatibility", tags=["compatibility"])

@router.post("/", response_model=BuildValidation)
async def test_compatibility(build: BuildComponents, service: CompatibilityService = Depends()):
    return service.test_compatibility(build)
