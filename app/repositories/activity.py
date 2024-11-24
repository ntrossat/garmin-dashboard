from app.repositories.base_repository import BaseRepository
from app.models import Activity


class ActivityRepository(BaseRepository):
    model = Activity
