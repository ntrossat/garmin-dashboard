from fastapi import FastAPI

from models import MessageResponse
from api.routes import activity

app = FastAPI()


@app.get("/")
def read_root() -> MessageResponse:
    return MessageResponse(message="Welcome to Garmin Dashboard!")


app.include_router(activity.router, prefix="/activities", tags=["Activities"])
