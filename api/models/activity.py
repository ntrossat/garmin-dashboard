from datetime import datetime

from sqlmodel import SQLModel, Field
from typing import Optional


class ActivityBase(SQLModel):
    name: str
    description: str
    type: Optional[str] = None
    start_date: datetime
    end_date: datetime


class Activity(ActivityBase, table=True):
    id: int = Field(nullable=False, primary_key=True)
