from .routes.versioning import v1

from fastapi import FastAPI

app = FastAPI()

app.include_router(v1)