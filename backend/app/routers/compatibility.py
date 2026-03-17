from app.core.dependencies import get_compatibility_service
from app.schemas import BuildComponents
from app.services.compatibility import CompatibilityService
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/comparitibility", tags=["comparitibility"])

@router.get("/")
async def test_compatibility(build: BuildComponents, service: CompatibilityService = Depends()):
    return await service.test_compatibility(build)
