from app.schemas.component import ComponentOfferResponse, ComponentResponse
from fastapi import APIRouter, Depends, Query
from app.core.dependencies import get_component_service
from app.services.components import ComponentService

router = APIRouter(prefix="/components", tags=["components"])

@router.get("/")
async def get_components(part_type: str = Query(None), query: str = Query(None), service: ComponentService = Depends(get_component_service)) -> list[ComponentResponse]:
    return await service.list(part_type, query)

@router.get("/{component_name}/offers")
async def get_component_offers(component_name: str, service: ComponentService = Depends(get_component_service)) -> list[ComponentOffer]:
    return await service.list_cheapest_offers_by_store(component_name)


