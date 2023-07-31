from fastapi import FastAPI

import models
from database import engine
from routers import post as post_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router.router, prefix='/posts', tags=['posts'])
