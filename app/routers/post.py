from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import get_db


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


router = APIRouter()


@router.get('/')
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {'data': posts}


@router.get('/{id}')
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    return {'data': post}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'data': new_post}


@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    post_to_delete = db.query(models.Post).filter(models.Post.id == id).first()
    if post_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    db.delete(post_to_delete)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}')
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found',
        )
    for key, value in updated_post.dict().items():
        setattr(post, key, value)
    db.commit()
    return {'data': post}
