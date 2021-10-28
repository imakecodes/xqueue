from typing import Optional

from pydantic import BaseModel


class PublishRequestSchema(BaseModel):
    payload: dict
    headers: Optional[dict] = None
    timestamp: Optional[int] = None
    http_method: Optional[str] = None
