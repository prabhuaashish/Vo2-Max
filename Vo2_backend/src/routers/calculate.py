from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import  get_db
from ..repository import calculations
from fastapi import Depends, Cookie


router = APIRouter(
    prefix="/calculate",
    tags=["Calculate"],
    responses={404: {"description": "Not found"}},
)

@router.post("/save-race-time/")
def save_race_time(data: schemas.RaceTimeCalculation, db: Session = Depends(get_db), user_id: str = Cookie()):
    race_predictions =  calculations.save_race_time(data, user_id, db)
    return race_predictions

@router.post("/race-time/")
def race_time(data: schemas.RaceTimeCalculation):
    race_predictions = calculations.calculate_race_time(data)
    return race_predictions

@router.post("/save-run-types/")
def save_run_types(data: schemas.RunType, db: Session = Depends(get_db), user_id: str = Cookie()):
    run_predictions = calculations.save_run_types(data, db, user_id)
    return run_predictions

@router.post("/run-types/")
def run_types(data: schemas.RunType):
    run_predictions = calculations.calculate_run_types(data)
    return run_predictions


@router.get("/daniels_old_run_types/")
def calculate(vo2_max: float, pace_type: str, pace_prediction_id: int):
    return calculations.daniels_old_run_types(vo2_max, pace_type, pace_prediction_id)


@router.get("/daniels_new_run_types/")
def calculate(vo2_max: float, pace_type: str, pace_prediction_id: int):
    return calculations.daniels_new_run_types(vo2_max, pace_type, pace_prediction_id)


@router.get("/pfitzinger_run_types/")
def calculate(vo2_max: float, pace_type: str, pace_prediction_id: int):
    return calculations.pfitzinger_run_types(vo2_max, pace_type, pace_prediction_id)


@router.get("/matt_fitzgerald_run_types/")
def calculate(vo2_max: float, pace_type: str, pace_prediction_id: int):
    return calculations.matt_fitzgerald_run_types(vo2_max, pace_type, pace_prediction_id)


