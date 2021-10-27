from fastapi import APIRouter

from app import __version__
from app.schemas.response import CommonMessageResponseSchema, HealthResponseSchema

api_router = APIRouter()


@api_router.get("/", response_model=CommonMessageResponseSchema, status_code=200)
def root() -> dict:
    """
    The root endpoint
    """
    return {"msg": "Hello messengers"}


@api_router.get("/health", response_model=HealthResponseSchema, status_code=200)
def health() -> dict:
    """
    The health check endpoint
    """
    return {"version": __version__}
