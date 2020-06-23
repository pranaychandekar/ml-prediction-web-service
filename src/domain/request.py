from pydantic import BaseModel


class Request(BaseModel):
    source: str
    text: str
