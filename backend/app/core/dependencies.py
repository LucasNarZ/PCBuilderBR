from typing import AsyncGenerator
from app.services.compatibility import CompatibilityService
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.clients import StoreClients
from app.core.database import AsyncSessionLocal
from app.services.components import ComponentService

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


def get_component_service(session: AsyncSession = Depends(get_session)) -> ComponentService:
    return ComponentService(session)


