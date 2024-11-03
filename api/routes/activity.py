from datetime import datetime
from typing import List, Any

from fastapi import APIRouter, HTTPException, Depends

from core.postgres.db import get_session, AsyncSession
from api.models.activity import Activity, ActivityCreate
from api.models.response import MessageResponse

router = APIRouter()


@router.get("/", response_model=List[Activity])
async def get_activities(
    session: AsyncSession = Depends(get_session),
) -> List[Activity]:
    """Get all activities."""
    return await Activity.get_all(session)


@router.get("/{id}", response_model=Activity)
async def get_activity(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> List[Activity]:
    """Get activity by ID."""
    activity = await Activity.get_by_id(id, session)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.post("/", response_model=Activity, status_code=201)
async def create_activity(
    activity: ActivityCreate, session: AsyncSession = Depends(get_session)
) -> Activity:
    """Create a new activity."""
    return await Activity.create(activity, session)


@router.put("/{id}", response_model=Activity)
async def update_activity(
    id: int,
    update: Activity,
    session: AsyncSession = Depends(get_session),
) -> Activity:
    """
    Update an existing activity.
    """
    activity = await Activity.get_by_id(id, session)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return await Activity.update(activity, update, session)


@router.delete("/{id}")
async def delete_item(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> MessageResponse:
    """
    Delete an item.
    """
    activity = await Activity.get_by_id(id, session)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    await Activity.delete(activity, session)
    return MessageResponse(message="Activity deleted successfully")
