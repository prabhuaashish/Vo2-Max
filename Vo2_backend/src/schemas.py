from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from datetime import datetime


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class StravaUser(BaseModel):
    name: str
    strava_id: int

    class Config:
        orm_mode = True

class UserDetails(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True

class StravaUserDetails(BaseModel):
    id: str
    name: str
    strava_id: str

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class RunType(BaseModel):
    race_distance: float
    units:str
    finish_time_hours: int
    finish_time_minutes: int
    finish_time_seconds: int
    pace_type: str
    type: str

    class Config:
        orm_mode = True

class RaceType(str, Enum):
    marathon = "marathon"
    half_marathon = "half_marathon"
    m10 = "10m"
    m10k = "10k"
    m5 = "5m"
    m5k = "5k"
    k3 = "3k"
    mile = "mile"
    m1500 = "1500"

class RaceTimeCalculation(BaseModel):
    frace: RaceType
    r1: RaceType
    r1t_hours: str
    r1t_minutes: str
    r1t_seconds: str
    r2: Optional[RaceType] = None
    r2t_hours: Optional[str] = None
    r2t_minutes: Optional[str] = None
    r2t_seconds: Optional[str] = None
    mpw: str
    dunits: str


    class Config:
        orm_mode = True

class DanielsOldRaceTimePredictionBase(BaseModel):
    id: int
    easy_run_pace: str
    tempo_run_pace: str
    vo2_max_pace: str
    speed_form_pace: str
    long_run_pace: str
    pace_prediction_id: int
    created_at: datetime
    updated_at: datetime

class DanielsNewRaceTimePredictionBase(BaseModel):
    id: int
    easy_run_pace: str
    marathon_pace: str
    threshold_pace: str
    interval_pace: str
    repetition_pace: str
    pace_prediction_id: int
    created_at: datetime
    updated_at: datetime

class PfitzingerRaceTimePredictionBase(BaseModel):
    id: int
    recovery_run_pace: str
    aerobic_run_pace: str
    long_medium_run_pace: str
    marathon_pace: str
    lactate_threshold_pace: str
    vo2max_pace: str
    pace_prediction_id: int
    created_at: datetime
    updated_at: datetime

class MattFitzgeraldRaceTimePredictionBase(BaseModel):
    id: int
    gray_zone_1_pace: str
    low_aerobic_run_pace: str
    moderate_aerobic_run_pace: str
    high_aerobic_run_pace: str
    threshold_pace: str
    gray_zone_3_pace: str
    vo2max_pace: str
    pace_prediction_id: int
    created_at: datetime
    updated_at: datetime


class RaceTimePredictionBase(BaseModel):
    id: int
    goal_race: str
    recent_race: str
    r1t_hours: int
    r1t_minutes: int
    r1t_seconds: int
    another_race: Optional[str]
    r2t_hours: Optional[int]
    r2t_minutes: Optional[int]
    r2t_seconds: Optional[int]
    milage_per_week: float
    dunits: str
    predicted_time: str
    pace_mile: str
    pace_km: str
    user_id: str
    created_at: datetime
    updated_at: datetime

class PacePredictionBase(BaseModel):
    id: int
    recent_race_distance: float
    units: str
    finish_time_hours: int
    finish_time_minutes: int
    finish_time_seconds: int
    pace_type: str
    type: str
    vdot: float
    user_id: str
    created_at: datetime
    updated_at: datetime
    daniels_old: Optional[DanielsOldRaceTimePredictionBase]
    daniels_new: Optional[DanielsNewRaceTimePredictionBase]
    pfitzinger: Optional[PfitzingerRaceTimePredictionBase]
    matt_fitzgerald: Optional[MattFitzgeraldRaceTimePredictionBase]

class UserRecords(BaseModel):
    race_records: List[RaceTimePredictionBase]
    pace_records: List[PacePredictionBase]
