from app.schemas.base import BaseSchema

class ComponentOfferResponse(BaseSchema):
    id: str
    price: float
    store: str
    url: str
    in_stock: bool

class ComponentResponse(BaseSchema):
    id: str
    name: str
    part_type: str
    brand: str
    specs: dict
    store_count: int
    best_offer: ComponentOfferResponse | None
