from fastapi import APIRouter

v1 = APIRouter(prefix='/api/v1')

@v1.get('/version')
async def healtz():
    return {'api_version': 'v1'}