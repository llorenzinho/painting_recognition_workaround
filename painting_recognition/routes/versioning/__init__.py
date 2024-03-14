from fastapi import APIRouter

from painting_recognition.routes.transformer.images import find_similar
from painting_recognition.core.DTO import image_dto as dto
from painting_recognition.core import logger

v1 = APIRouter(prefix='/api/v1')

@v1.get('/version')
async def healtz():
    return {'api_version': 'v1'}

@v1.post('/find_similar')
async def _find_similar(image: dto.ImageSimilarityDTO):
    return find_similar(image)