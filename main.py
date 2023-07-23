from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of posts1",
            "content": "content of post1",
            "id": 1},
            {"title": "title of posts2",
            "content": "content of post2",
            "id": 2}]

@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/posts')
def get_posts():
    return {'data': my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict} 
