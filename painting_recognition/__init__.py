from .routes.versioning import *

from fastapi import FastAPI

app = FastAPI()

@app.get('/healthz')
async def healtz():
    return {'status': 'OK'}

app.include_router(v1) # v1 api version