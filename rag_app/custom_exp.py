from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from .logger_config import set_logging,get_logger

set_logging(log_file="query.log", mode="w")
logger = get_logger(__name__)

async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.error(f"Validation error: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )