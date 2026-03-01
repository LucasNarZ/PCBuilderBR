from fastapi import APIRouter, Depends
from app.core.dependencies import get_component_service
from app.services.components import ComponentService


router = APIRouter(prefix="/components", tags=["components"])

@router.get("/")
async def get_components(service: ComponentService = Depends(get_component_service)):
    return await service.list()
