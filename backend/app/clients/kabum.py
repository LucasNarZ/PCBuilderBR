import httpx
from app.clients.base import StoreClientProtocol, StoreProduct


class KabumClient:
    BASE_URL = "https://servicespub.prod.api.aws.grupokabum.com.br"

    def __init__(self) -> None:
        self._headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

    def _to_store_product(self, item: dict) -> StoreProduct:
        attrs = item.get("attributes", {})
        offer = attrs.get("offer") or {}
        images = attrs.get("images") or []
        price = offer.get("price_with_discount") or attrs.get("price_with_discount", 0.0)

        return StoreProduct(
            external_id=str(item.get("id")),
            name=attrs.get("title", ""),
            price=price,
            url=f"https://www.kabum.com.br/produto/{item.get('id')}/{attrs.get('product_link', '')}",
            in_stock=attrs.get("available", False),
            image_url=images[0] if images else None,
        )

    async def search(self, query: str) -> list[StoreProduct]:
        params = {
            "query": query,
            "page_number": 1,
            "page_size": 20,
            "sort": "most_searched",
            "is_prime": "false",
            "variant": "null",
            "facet_filters": "",
            "payload_data": "products_category_filters",
            "include": "gift",
        }
        async with httpx.AsyncClient(headers=self._headers) as client:
            response = await client.get(f"{self.BASE_URL}/catalog/v2/search", params=params)
            response.raise_for_status()
            data = response.json()
            return [
                self._to_store_product(item)
                for item in data.get("data", [])
                if item.get("type") == "product"
            ]

    async def get_product(self, product_id: str) -> StoreProduct | None:
        async with httpx.AsyncClient(headers=self._headers) as client:
            response = await client.get(f"{self.BASE_URL}/catalog/v2/products/{product_id}")
            if response.status_code == 404:
                return None
            response.raise_for_status()
            item = response.json().get("data", {})
            return self._to_store_product(item) if item else None


def is_valid_client(client: StoreClientProtocol) -> None:
    pass


is_valid_client(KabumClient())
