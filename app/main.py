from fastapi import FastAPI

from app.resources.health import api_router as health_router
from app.resources.publish import api_router as publish_router

app = FastAPI()


app.include_router(health_router)
app.include_router(publish_router, prefix="/publish")
