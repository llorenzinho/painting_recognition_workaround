from fastapi import APIRouter
from painting_recognition.core import logger

v1 = APIRouter(prefix='/api/v1')

@v1.get('/healtz')
async def healtz():
    logger.debug('Healtz check')
    return {'api_version': 'v1'}