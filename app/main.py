from fastapi import FastAPI

from api_router import api_router
from app.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(api_router)
