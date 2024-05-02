from pydantic import BaseModel


class AuthData(BaseModel):
    token: str
    user: str

class DefaultData(BaseModel):
    id: int
    info: dict
    tags: list
    text: str
    updated_by: str
    url: str