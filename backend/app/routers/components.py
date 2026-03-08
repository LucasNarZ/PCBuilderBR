from fastapi import APIRouter, Depends, Query
from app.core.dependencies import get_component_service
from app.services.components import ComponentService


router = APIRouter(prefix="/components", tags=["components"])

@router.get("/")
async def get_components(part_type: str = Query(None), service: ComponentService = Depends(get_component_service)):
    return await service.list(part_type)


