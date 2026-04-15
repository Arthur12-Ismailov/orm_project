from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    user_id: int

class UserCreate(BaseModel):
    name: str