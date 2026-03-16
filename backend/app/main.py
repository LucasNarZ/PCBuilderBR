from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.jobs import update_products_prices

from app.core.database import engine
from app.core.database import Base
from app.routers import components

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    scheduler.add_job(update_products_prices, "cron", hour=3, minute=0)
    scheduler.start()
    yield
    scheduler.shutdown()
    await engine.dispose()


app = FastAPI(lifespan=lifespan, docs_url="/docs", root_path="/api")

app.include_router(components.router)
