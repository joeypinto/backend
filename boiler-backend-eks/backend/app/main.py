from app.core.config import settings
from fastapi import FastAPI
# import logging
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.core.logging_setup import setup_root_logger
from fastapi_redis_cache import FastApiRedisCache
from fastapi import FastAPI, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
import os
import redis
from datetime import timedelta, datetime
from app.lib.redis_util import RedisClient
from app.lib.util_mail import Email
# import sentry_sdk

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

#setup root logger
setup_root_logger()
#Get logger for module
LOGGER = logging.getLogger(__name__)
LOGGER.info("---Starting App---")

# sentry_sdk.init(
#     dsn="https://921cbc79fc5a09fbaa8ba3d89aa2dc83@o4505471231328256.ingest.sentry.io/4505711601647616",

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production,
#     traces_sample_rate=1.0,
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix=settings.API_V1_STR)

LOCAL_REDIS_URL = "redis://:devpassword@redis:6379"

@app.get("/health")
async def health():
    return {"message": "OK"}

@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session, AsyncSession]
    )
        