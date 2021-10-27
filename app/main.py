from fastapi import FastAPI

from app.resources.health import api_router as health_router

app = FastAPI()


app.include_router(health_router)
