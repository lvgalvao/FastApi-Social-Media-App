import time
from random import randrange
from typing import Optional

import psycopg2
from fastapi import FastAPI, HTTPException, Response, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


create_table_sql = """
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    published BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
"""

while True:
    try:
        conn = psycopg2.connect(
            host='postgres',
            database='curso',
            user='postgres',
            password='mysecretpassword',
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print('Database connection was succesfull!')
        break
    except Exception as error:
        print('Connection to database failed')
        print('Error :', error)
        time.sleep(2)


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * from posts""")
    posts = cursor.fetchall()
    return {'data': posts}


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * from posts WHERE id = %s""", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    return {'data': post}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING id""",
        (post.title, post.content, post.published),
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {'data': new_post}


@app.delete('/posts/{id}')
def delete_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    post_to_delete = cursor.fetchone()
    if post_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    cursor.execute("""DELETE FROM posts WHERE id = %s""", (id,))
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):

    cursor.execute(
        """UPDATE posts set title = %s, content = %s, published = %s where id = %s RETURNING *""",
        (post.title, post.content, post.published, id),
    )
    post_to_update = cursor.fetchone()
    if post_to_update == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )

    return {'data': post_to_update}
