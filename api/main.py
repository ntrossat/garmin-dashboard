from fastapi import FastAPI

from app.models import MessageResponse
from app.routes import activity

app = FastAPI()


@app.get("/")
def read_root() -> MessageResponse:

    return MessageResponse(message="Welcome to Garmin Dashboard!")


app.include_router(activity.router, prefix="/activities", tags=["Activities"])
