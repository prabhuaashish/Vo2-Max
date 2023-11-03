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

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    raceprediction = relationship("RaceTimePrediction", back_populates="user")
    pace_predictions = relationship("PacePrediction", back_populates="user")


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



class PacePrediction(Base):
    __tablename__ = "pace_predictions"  

    id = Column(Integer, primary_key=True, index=True)
    recent_race_distance = Column(Float)  # Recent Race Distance
    units = Column(String(255))  # Units (e.g., 'km' or 'miles')
    finish_time_hours = Column(Integer)  # Finish Time Hours
    finish_time_minutes = Column(Integer)  # Finish Time Minutes
    finish_time_seconds = Column(Integer)  # Finish Time Seconds
    pace_type = Column(String(255))  # Display Training Paces (e.g., 'min/mile' or 'min/km')
    type = Column(String(255))  # Type (e.g., 'Daniels_old', 'Daniels_new', 'Pfitzinger', 'Matt_Fitzgerald')

    vdot = Column(Float)  # VDOT

    # Relationship to DanielsOldRaceTimePrediction
    daniels_old = relationship("DanielsOldRaceTimePrediction", back_populates="pace_prediction", uselist=False)

    # Relationship to DanielsNewRaceTimePrediction
    daniels_new = relationship("DanielsNewRaceTimePrediction", back_populates="pace_prediction", uselist=False)

    # Relationship to PfitzingerRaceTimePrediction
    pfitzinger = relationship("PfitzingerRaceTimePrediction", back_populates="pace_prediction", uselist=False)

    # Relationship to MattFitzgeraldRaceTimePrediction
    matt_fitzgerald = relationship("MattFitzgeraldRaceTimePrediction", back_populates="pace_prediction", uselist=False)

    # Relationship to User
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="pace_predictions")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DanielsOldRaceTimePrediction(Base):
    __tablename__ = "daniels_old_predictions"

    id = Column(Integer, primary_key=True, index=True)
    easy_run_pace = Column(String(255))
    tempo_run_pace = Column(String(255))
    vo2_max_pace = Column(String(255))
    speed_form_pace = Column(String(255))
    long_run_pace = Column(String(255))

    # Relationship to PacePrediction
    pace_prediction_id = Column(Integer, ForeignKey("pace_predictions.id"))
    pace_prediction = relationship("PacePrediction", back_populates="daniels_old")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class DanielsNewRaceTimePrediction(Base):
    __tablename__ = "daniels_new_predictions"

    id = Column(Integer, primary_key=True, index=True)
    easy_run_pace = Column(String(255))
    marathon_pace = Column(String(255))
    threshold_pace = Column(String(255))
    interval_pace = Column(String(255))
    repetition_pace = Column(String(255))

    # Relationship to PacePrediction
    pace_prediction_id = Column(Integer, ForeignKey("pace_predictions.id"))
    pace_prediction = relationship("PacePrediction", back_populates="daniels_new")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class PfitzingerRaceTimePrediction(Base):
    __tablename__ = "pfitzinger_predictions"

    id = Column(Integer, primary_key=True, index=True)
    recovery_run_pace = Column(String(255))
    aerobic_run_pace = Column(String(255))
    long_medium_run_pace = Column(String(255))
    marathon_pace = Column(String(255))
    lactate_threshold_pace = Column(String(255))
    vo2max_pace = Column(String(255))

    # Relationship to PacePrediction
    pace_prediction_id = Column(Integer, ForeignKey("pace_predictions.id"))
    pace_prediction = relationship("PacePrediction", back_populates="pfitzinger")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class MattFitzgeraldRaceTimePrediction(Base):
    __tablename__ = "matt_fitzgerald_predictions"

    id = Column(Integer, primary_key=True, index=True)
    gray_zone_1_pace = Column(String(255))
    low_aerobic_run_pace = Column(String(255))
    moderate_aerobic_run_pace = Column(String(255))
    high_aerobic_run_pace = Column(String(255))
    threshold_pace = Column(String(255))
    gray_zone_3_pace = Column(String(255))
    vo2max_pace = Column(String(255))

    # Relationship to PacePrediction
    pace_prediction_id = Column(Integer, ForeignKey("pace_predictions.id"))
    pace_prediction = relationship("PacePrediction", back_populates="matt_fitzgerald")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)