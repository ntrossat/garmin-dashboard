from repository.abstract import AbstractRepository
from models import Activity


class ActivityRepository(AbstractRepository):
    model = Activity
