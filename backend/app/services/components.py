from __future__ import annotations
from app.models.component import ComponentOffer
from app.schemas.component import ComponentOfferResponse, ComponentResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from app.models import Component


class ComponentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, part_type: str | None = None, search: str | None = None) -> list[ComponentResponse]:
        subquery = (
            select(
                ComponentOffer.component_id,
                func.count(func.distinct(ComponentOffer.store)).label("store_count"),
                func.min(ComponentOffer.price).label("cheapest_price")
            )
            .where(ComponentOffer.in_stock == True)
            .group_by(ComponentOffer.component_id)
            .subquery()
        )

        query = (
            select(Component, subquery.c.store_count, ComponentOffer)
            .outerjoin(subquery, Component.id == subquery.c.component_id)
            .outerjoin(
                ComponentOffer,
                (ComponentOffer.component_id == Component.id) &
                (ComponentOffer.price == subquery.c.cheapest_price)
            )
        )


        if part_type and search:
            query.where(Component.part_type == part_type, Component.name.ilike(f"%{search}%"))
        elif part_type:
            query.where(Component.part_type == part_type)
        elif search:
            query.where(Component.name.ilike(f"%{search}%"))

        result = await self.session.execute(query)

        return [
            ComponentResponse.model_validate({
                **component.__dict__,
                "storeCount": store_count or 0,
                "bestOffer": offer
            })
            for component, store_count, offer in result.all()
        ]

    async def list_cheapest_offers_by_store(self, component_name: str) -> list[ComponentOfferResponse]:
        subquery = (
            select(
                ComponentOffer.store,
                func.min(ComponentOffer.price).label("min_price"),
            )
            .join(Component, Component.id == ComponentOffer.component_id)
            .where(Component.name == component_name)
            .where(ComponentOffer.in_stock == True)
            .group_by(ComponentOffer.store)
            .subquery()
        )

        result = await self.session.execute(
            select(ComponentOffer)
            .join(Component, Component.id == ComponentOffer.component_id)
            .join(subquery, (ComponentOffer.store == subquery.c.store) & (ComponentOffer.price == subquery.c.min_price))
            .where(Component.name == component_name)
        )

        return [ComponentOfferResponse.model_validate(offer) for offer in result.scalars().all()]
