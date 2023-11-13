from pydantic import BaseModel
from enum import Enum
from typing import Optional, List


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    user_id: str
    name: str
    email: str
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class UserDetails(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True

# class User(BaseModel):
#     id: str

#     class Config:
#         orm_mode = True


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
    # user: User

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
    # user: str = 


    class Config:
        orm_mode = True



