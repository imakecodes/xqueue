from fastapi import APIRouter, Body

from app.schemas.response import CommonMessageResponseSchema
from app.tasks import publish_message

api_router = APIRouter()


@api_router.post(
    "/{project}/{queue}",
    response_model=CommonMessageResponseSchema,
    status_code=200,
    tags=["publish"],
    summary="Publish a new message",
    description="Receives the message and saves on queue service",
    response_description="Response message",
)
def publish_post(project: str, queue: str, body: dict = Body(...)) -> dict:
    """
    Receives the GET request that will be proxyed to subscribers
    """

    queue = f"{project}-{queue}"
    publish_message.s(project, queue, body).apply_async(queue=queue)
    return {"msg": "Received"}
