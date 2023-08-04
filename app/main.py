from fastapi import FastAPI

from routers import post as post_router
from routers import user as user_router

app = FastAPI()

app.include_router(post_router.router, prefix='/posts', tags=['posts'])
app.include_router(user_router.router, prefix='/users', tags=['users'])
