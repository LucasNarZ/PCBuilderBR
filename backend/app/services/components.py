from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Component

class ComponentService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def list(self, part_type: str | None = None):
        if part_type:
            result = await self.session.execute(select(Component).where(Component.part_type == part_type))
            return result.scalars().all()

        result = await self.session.execute(select(Component))
        return result.scalars().all()
                
