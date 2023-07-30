from fastapi import FastAPI
from routers import post as post_router

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router.router, prefix="/posts", tags=["posts"])
