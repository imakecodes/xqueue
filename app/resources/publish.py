from fastapi import APIRouter

from app.schemas.response import CommonMessageResponseSchema

api_router = APIRouter()


@api_router.post(
    "",
    response_model=CommonMessageResponseSchema,
    status_code=200,
    tags=["publish"],
    summary="Publish a new message",
    description="Receives the message and saves on queue service",
    response_description="Response message",
)
def publish_post() -> dict:
    """
    Receives the GET request that will be proxyed to subscribers
    """
    return {"msg": "Received"}
