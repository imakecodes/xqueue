from fastapi import APIRouter

from app import __version__
from app.schemas.response import CommonMessageResponseSchema
from app.services.rabbit_api import RabbitApi

api_router = APIRouter()


@api_router.get(
    "/topics",
    response_model=CommonMessageResponseSchema,
    status_code=200,
    tags=["admin"],
    summary="Topic list",
    description="List all topis available on RabbitMQ",
)
def root() -> dict:
    """
    Admin:
    """

    rabbit = RabbitApi()
    response = []
    rabbit.load_queues_info()
    return {"msg": "Hello messengers"}
