from typing import Union, List

from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

from core.postgres.db import get_session

from api.models.activity import Activity
from api.routes import activity


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


app.include_router(activity.router, prefix="/activities", tags=["Activities"])
