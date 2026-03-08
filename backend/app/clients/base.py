from pydantic import BaseModel
from typing import Protocol

class StoreProduct(BaseModel):
    external_id: str
    name: str
    price: float
    url: str
    in_stock: bool
    image_url: str | None = None


class StoreClientProtocol(Protocol):
    async def search(self, query: str) -> list[StoreProduct]: ...
    async def get_product(self, product_id: str) -> StoreProduct | None: ...
