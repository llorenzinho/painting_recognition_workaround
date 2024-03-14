from .routes.versioning import v1

from fastapi import FastAPI

from painting_recognition.core import logger
from painting_recognition.core.config import app_config as cfg
from painting_recognition.core.clients import CustomQdrant

async def lifespan(app: FastAPI):
    logger.info('Application starting')
    logger.info(f'Application config loaded: {cfg.model_dump()}')
    logger.info('Checking QdrantClient collection')
    client = CustomQdrant()
    await client.init_collection()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/healthz')
async def healtz():
    return {'status': 'OK'}

app.include_router(v1) # v1 api version
