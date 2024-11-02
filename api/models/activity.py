from datetime import datetime

from sqlmodel import SQLModel, Field
from typing import Optional


class Activity(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    type: Optional[str] = None
    start_date: datetime
    end_date: datetime
