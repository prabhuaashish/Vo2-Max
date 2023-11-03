from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas
from ..database import  get_db
from ..repository import calculations



router = APIRouter(
    prefix="/calculate",
    tags=["Calculate"],
    responses={404: {"description": "Not found"}},
)

@router.post("/race-time/")
def race_time(data: schemas.RaceTimeCalculation, db: Session = Depends(get_db)):
    race_predictions =  calculations.calculate_race_time(data, db)
    return race_predictions

@router.post("/run-types/")
def run_types(data: schemas.RunType, db: Session = Depends(get_db)):
    run_predictions = calculations.calculate_run_types(data, db)
    return run_predictions


@router.get("/daniels_old_run_types/")
def calculate(vo2_max: float, pace_type: str, db: Session = Depends(get_db)):
    return calculations.daniels_old_run_types(vo2_max, pace_type)


@router.get("/daniels_new_run_types/")
def calculate(vo2_max: float, pace_type: str, db: Session = Depends(get_db)):
    return calculations.daniels_new_run_types(vo2_max, pace_type)


@router.get("/pfitzinger_run_types/")
def calculate(vo2_max: float, pace_type: str, db: Session = Depends(get_db)):
    return calculations.pfitzinger_run_types(vo2_max, pace_type)


@router.get("/matt_fitzgerald_run_types/")
def calculate(vo2_max: float, pace_type: str, db: Session = Depends(get_db)):
    return calculations.matt_fitzgerald_run_types(vo2_max, pace_type)


