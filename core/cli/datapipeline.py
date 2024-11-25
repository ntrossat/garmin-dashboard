import datetime
from garminconnect import Garmin

from app.models import Activity


class DataPipeline:
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._data_source = None
        self._garmin = Garmin(user, password)
        self._garmin.login()

    def set_data_source(self, data_source):
        self._data_source

    def fetch_raw_data(self):
        # start_date = datetime.date(1970, 1, 1)
        start_date = datetime.date(2024, 11, 20)
        end_date = datetime.date(2024, 11, 24)

        activities = self._garmin.get_activities_by_date(
            start_date.isoformat(), end_date.isoformat(), "running"
        )

        for activity in activities:
            activity = Activity.model_validate(activity)
            print(activity)
            exit()
        return "Well done!"

        # Voir dbt pour transformation des données
