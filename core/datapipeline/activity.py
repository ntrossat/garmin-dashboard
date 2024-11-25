import os
import datetime
from garminconnect import Garmin

from models import ActivityRaw


class ActivityPipeline:
    def __init__(self):
        user = os.getenv("GARMIN_USERNAME")
        password = os.getenv("GARMIN_PASSWORD")
        garmin = Garmin(user, password)
        garmin.login()

        self._garmin = garmin

    def load_raw_data(self):
        # start_date = datetime.date(1970, 1, 1)
        start_date = datetime.date(2024, 11, 20)
        end_date = datetime.date(2024, 11, 24)

        activities = self._garmin.get_activities_by_date(
            start_date.isoformat(), end_date.isoformat(), "running"
        )

        for activity in activities:
            activity = ActivityRaw.model_validate(activity)
        return "Well done!"

        # Voir dbt pour transformation des données
