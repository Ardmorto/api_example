from pydantic import BaseModel

class AllMemesData(BaseModel):
    id:  int
    info: dict
    tags: list
    text: str
    url: str
    updated_by: str

class AllMemes(BaseModel):
    data: AllMemesData

class AuthData(BaseModel):
    token: str
    user: str