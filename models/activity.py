import uuid
from datetime import datetime

from sqlmodel import SQLModel, Field, UniqueConstraint, DateTime, MetaData


class ActivityBase(SQLModel):
    name: str
    description: str
    type: str
    start_at: datetime = Field(sa_type=DateTime(timezone=True))
    end_at: datetime = Field(sa_type=DateTime(timezone=True))

    __table_args__ = (
        UniqueConstraint("type", "start_at", name="unique_type_start_at"),
    )


class Activity(ActivityBase, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)


class ActivityRaw(SQLModel, table=False):
    activityId: int
    activityName: str
    startTimeLocal: str
    startTimeGMT: str
    activityType: dict
    eventType: dict
    distance: float
    duration: float
    elapsedDuration: float
    movingDuration: float
    elevationGain: float
    elevationLoss: float
    averageSpeed: float
    maxSpeed: float
    startLatitude: float
    startLongitude: float
    hasPolyline: bool
    hasImages: bool
    ownerId: int
    ownerDisplayName: str
    ownerFullName: str
    ownerProfileImageUrlSmall: str
    ownerProfileImageUrlMedium: str
    ownerProfileImageUrlLarge: str
    calories: float
    bmrCalories: float
    averageHR: float
    maxHR: float
    averageRunningCadenceInStepsPerMinute: float
    maxRunningCadenceInStepsPerMinute: float
    steps: int
    userRoles: list
    privacy: dict
    userPro: bool
    hasVideo: bool
    timeZoneId: int
    beginTimestamp: int
    sportTypeId: int
    avgStrideLength: float
    vO2MaxValue: float
    deviceId: int
    minElevation: float
    maxElevation: float
    maxDoubleCadence: float
    summarizedDiveInfo: dict
    maxVerticalSpeed: float
    manufacturer: str
    locationName: str
    lapCount: int
    endLatitude: float
    endLongitude: float
    waterEstimated: float
    minActivityLapDuration: float
    splitSummaries: list
    hasSplits: bool
    moderateIntensityMinutes: int
    vigorousIntensityMinutes: int
    hasHeatMap: bool
    fastestSplit_1000: float
    fastestSplit_1609: float
    purposeful: bool
    manualActivity: bool
    pr: bool
    autoCalcCalories: bool
    elevationCorrected: bool
    atpActivity: bool
    favorite: bool
    decoDive: bool
    parent: bool

    metadata = MetaData(schema="source")
