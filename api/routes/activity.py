import uuid

from fastapi import APIRouter, HTTPException, Depends

from core.postgres.db import get_session, AsyncSession
from models import Activity, ActivityInput, MessageResponse
from repositories import ActivityRepository

router = APIRouter()


@router.get("/", response_model=list[Activity])
async def get_activities(
    session: AsyncSession = Depends(get_session),
) -> list[Activity]:
    """Get all activities."""
    return await ActivityRepository.list(session)


@router.get("/{id}", response_model=Activity)
async def get_activity(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
) -> Activity:
    """Get activity by ID."""
    activity = await ActivityRepository.get(session, id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.post("/", response_model=Activity, status_code=201)
async def create_activity(
    activity: ActivityInput, session: AsyncSession = Depends(get_session)
) -> Activity:
    """Create a new activity."""
    activity = Activity.model_validate(activity)
    return await ActivityRepository.save(session, activity)


@router.put("/{id}", response_model=Activity)
async def update_activity(
    id: uuid.UUID,
    activity: ActivityInput,
    session: AsyncSession = Depends(get_session),
) -> Activity:
    """
    Update an existing activity.
    """
    activity_db = await ActivityRepository.get(session, id)

    if not activity_db:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = Activity.model_validate(activity)
    activity.id = id
    activity_db.sqlmodel_update(activity)

    return await ActivityRepository.save(session, activity_db)


@router.delete("/{id}")
async def delete_activity(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
) -> MessageResponse:
    """
    Delete an activity.
    """
    activity = await ActivityRepository.get(session, id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    await ActivityRepository.delete(session, activity)
    return MessageResponse(message="Activity deleted successfully")
