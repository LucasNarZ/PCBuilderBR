from app.schemas import BuildComponents
from app.services.compatibility import CompatibilityService
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/compatibility", tags=["compatibility"])

@router.post("/")
async def test_compatibility(build: BuildComponents, service: CompatibilityService = Depends()):
    return service.test_compatibility(build)
