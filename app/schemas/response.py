from pydantic import BaseModel


class CommonMessageResponseSchema(BaseModel):
    msg: str


class HealthResponseSchema(BaseModel):
    version: str
