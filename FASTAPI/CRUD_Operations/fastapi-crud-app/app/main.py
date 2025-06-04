from fastapi import FastAPI
from .database import engine
from . import models
from .routers import items

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}