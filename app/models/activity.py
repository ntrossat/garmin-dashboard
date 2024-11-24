import uuid
from datetime import datetime

from sqlmodel import SQLModel, Field, UniqueConstraint, DateTime

class ActivityInput(SQLModel):
    name: str
    description: str
    type: str
    start_at: datetime = Field(sa_type=DateTime(timezone=True)) 
    end_at: datetime = Field(sa_type=DateTime(timezone=True)) 

    __table_args__ = (
        UniqueConstraint("type", "start_at", name="unique_type_start_at"),
    )


class Activity(ActivityInput, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)