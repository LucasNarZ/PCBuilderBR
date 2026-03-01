from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.component import Component

class ComponentService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def list(self):
        result = await self.session.execute(select(Component))
        return result.scalars().all()
                
