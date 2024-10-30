from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

from core.postgres.db import init_db, get_session
from api.models.activity import Activity

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


# TODO Replaced with Alembic

# @app.on_event("startup")
# def on_startup():
#     await init_db()


@app.get("/activities", response_model=List[Activity])
async def get_activities(*, session: Session = Depends(get_session)):
    response = await session.exec(select(Activity))
    activities = response.scalars().all()
    print("hello")
    return activities


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item, session: Session = Depends(get_session)) -> Item:
#     return item


# @app.get("/items/", response_model=list[Item])
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
