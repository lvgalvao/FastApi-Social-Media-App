from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='mysecretpassword', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error :", error)
        time.sleep(2)
    
my_posts = [
    {'title': 'title of posts1', 'content': 'content of post1', 'id': 1},
    {'title': 'title of posts2', 'content': 'content of post2', 'id': 2},
]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/posts')
def get_posts():
    return {'data': my_posts}


@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'post with id: {id} was not found'}
    return {'data': post}


@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {'data': post_dict}


@app.delete('/posts/{id}')
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )

    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}
