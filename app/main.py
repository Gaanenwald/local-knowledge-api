from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.concurrency import run_in_threadpool

from api_router import api_router
from app.config import settings
from services.transformers_tokenizer import TransformersTokenizer


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        tokenizer = await run_in_threadpool(
            TransformersTokenizer,
            model_name="BAAI/bge-m3",
        )
    except Exception as e:
        print("Failed to initialize tokenizer")
        raise
    print("Tokenizer initialized successfully")
    yield {"tokenizer": tokenizer}


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(api_router)
