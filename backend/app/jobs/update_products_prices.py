import asyncio
from datetime import datetime
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.clients import StoreClients
from app.core.dependencies import get_session
from app.models import Component, ComponentOffer

async def update_products_prices(
    session: AsyncSession = Depends(get_session),
    store_clients: StoreClients = Depends(),
):
    result = await session.execute(select(Component))
    components = result.scalars().all()

    searches = [store_clients.kabum.search(component.name) for component in components]
    results = await asyncio.gather(*searches)

    for component, store_products in zip(components, results):
        if not store_products:
            print(f"Component {component.name} not founded.")
            continue
        for product in store_products:

            offer = ComponentOffer(
                id=product.external_id,
                component_id=component.id,
                price=product.price,
                store="kabum",
                url=product.url,
                in_stock=product.in_stock,
                last_updated=datetime.utcnow(),
            )
            await session.merge(offer)

    await session.commit()


if __name__ == "__main__":
    from app.core.database import AsyncSessionLocal

    async def main():
        async with AsyncSessionLocal() as session:
            await update_products_prices(
                session=session,
                store_clients=StoreClients(),
            )

    asyncio.run(main())
