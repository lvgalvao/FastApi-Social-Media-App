from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


# Enherit PostBase
class PostCreate(PostBase):
    pass


# Response model
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
