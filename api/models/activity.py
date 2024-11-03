from datetime import datetime
from typing import List


from sqlmodel import SQLModel, Field, select, UniqueConstraint
from sqlmodel.ext.asyncio.session import AsyncSession


class ActivityCreate(SQLModel):
    name: str
    description: str
    type: str
    start_date: str | None = None
    end_date: str | None = None

    __table_args__ = (
        UniqueConstraint("type", "start_date", name="unique_type_start_date"),
    )


class ActivityModel(ActivityCreate):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())


class Activity(ActivityModel, table=True):

    @staticmethod
    async def get_all(session: AsyncSession) -> list[ActivityModel]:
        response = await session.exec(select(Activity))
        return response.all()

    @staticmethod
    async def get_by_id(id: int, session: AsyncSession) -> ActivityModel | None:
        activity = await session.get(Activity, id)
        return activity

    @staticmethod
    async def create(activity: ActivityModel, session: AsyncSession) -> ActivityModel:
        activity = Activity.model_validate(activity)
        session.add(activity)
        await session.commit()
        await session.refresh(activity)
        return activity

    @staticmethod
    async def update(
        activity: ActivityModel, update: ActivityModel, session: AsyncSession
    ) -> ActivityModel:
        update_data = Activity.model_validate(update)
        activity.sqlmodel_update(update_data)
        session.add(activity)
        await session.commit()
        await session.refresh(activity)
        return activity

    @staticmethod
    async def delete(activity: ActivityModel, session: AsyncSession) -> None:
        await session.delete(activity)
        await session.commit()
