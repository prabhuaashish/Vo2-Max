from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True) 
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    raceprediction = relationship("RaceTimePrediction", back_populates="user")


class RaceTimePrediction(Base):
    __tablename__ = "race_time_predictions"

    id = Column(Integer, primary_key=True, index=True)
    goal_race = Column(String(255), index=True)
    recent_race = Column(String(255), index=True)
    r1t_hours = Column(Integer)
    r1t_minutes = Column(Integer)
    r1t_seconds = Column(Integer)
    another_race = Column(String(255))
    r2t_hours = Column(Integer)
    r2t_minutes = Column(Integer)
    r2t_seconds = Column(Integer)
    milage_per_week = Column(Float)
    dunits = Column(String(255))
    predicted_time = Column(String(255))
    pace_mile = Column(String(255))
    pace_km = Column(String(255))

    user_id = Column(Integer, ForeignKey("users.id"))
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="raceprediction")


