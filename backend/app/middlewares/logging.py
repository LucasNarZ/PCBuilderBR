from app.core.logging import get_logger
import structlog
from fastapi import Request
import time
import uuid

logger = get_logger()

async def logging_middleware(request: Request, call_next):
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        request_id=str(uuid.uuid4()),
        method=request.method,
        path=request.url.path,
    )

    start = time.perf_counter()
    try:
        response = await call_next(request)
        duration = round(time.perf_counter() - start, 4)
        structlog.contextvars.bind_contextvars(
            status_code=response.status_code,
            duration_seconds=duration,
        )
        logger.info("http_request")
        return response
    except Exception:
        duration = round(time.perf_counter() - start, 4)
        structlog.contextvars.bind_contextvars(duration_seconds=duration)
        logger.exception("http_request_failed")
        raise
