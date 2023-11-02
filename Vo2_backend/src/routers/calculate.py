from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas
from ..database import engine, get_db
from ..hashing import Hash
from ..repository import calculations


router = APIRouter(
    prefix="/calculate",
    tags=["Calculate"],
    responses={404: {"description": "Not found"}},
)


@router.post("/run-types/")
def calculate(data: schemas.RunType, db: Session = Depends(get_db)):
    return calculations.calculate_run_types(data)


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


@router.post("/race-time/")
def calculate(data: schemas.RaceTimeCalculation, db: Session = Depends(get_db)):
    return calculations.calculate_race_time(data)