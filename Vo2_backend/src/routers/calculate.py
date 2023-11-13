from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import  get_db
from ..repository import calculations
from ..models import User
from fastapi import Depends, FastAPI, HTTPException, Request, Cookie

"""
curl -X 'POST' \
  'http://127.0.0.1:8000/calculate/race-time/' \
  -H 'accept: application/json' \
  -H 'Cookie: user_id=cdac7ac8-118e-4994-ab9b-ac77a4893b0f' \
  -H 'Content-Type: application/json' \
  -d '{
  "frace": "marathon",
  "r1": "10k",
  "r1t_hours": "0",
  "r1t_minutes": "56",
  "r1t_seconds": "52",
  "r2": "5k",
  "r2t_hours": "0",
  "r2t_minutes": "27",
  "r2t_seconds": "51",
  "mpw": "40",
  "dunits": "km"
}'
"""

router = APIRouter(
    prefix="/calculate",
    tags=["Calculate"],
    responses={404: {"description": "Not found"}},
)
# def get_user_id_from_cookie(request: Request):
#     print("Request Headers:", request.headers)
#     user_id = request.cookies.get("user_id")
#     print("USER ID", user_id)
#     if user_id is None:
#         raise HTTPException(status_code=400, detail="Session ID not found in cookie")
#     return user_id

def get_user_id_from_cookie(user_id: str = Cookie(alias="user_id")):
    if user_id is None:
        raise HTTPException(status_code=401, detail="User ID not found in cookie")
    return user_id

@router.post("/race-time/")
# def race_time(data: schemas.RaceTimeCalculation, db: Session = Depends(get_db), user_id: str = Depends(get_user_id_from_cookie)):
def race_time(data: schemas.RaceTimeCalculation, db: Session = Depends(get_db), user_id: str = Cookie()):
    # print("Request Headers:", request.headers)
    print("User ID in route: ", user_id)
    race_predictions =  calculations.calculate_race_time(data, user_id, db)
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


