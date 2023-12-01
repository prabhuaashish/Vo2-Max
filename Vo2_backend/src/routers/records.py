from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    tags=["Records"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}/records", response_model=schemas.UserRecords)
def get_user_records(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    race_records = db.query(models.RaceTimePrediction).filter(models.RaceTimePrediction.user_id == user_id).all()
    pace_records = db.query(models.PacePrediction).filter(models.PacePrediction.user_id == user_id).all()

        # Fetch related data for each PacePrediction record
    for pace_record in pace_records:
        pace_record.daniels_old = db.query(models.DanielsOldRaceTimePrediction).filter(
            models.DanielsOldRaceTimePrediction.pace_prediction_id == pace_record.id
        ).first()
        pace_record.daniels_new = db.query(models.DanielsNewRaceTimePrediction).filter(
            models.DanielsNewRaceTimePrediction.pace_prediction_id == pace_record.id
        ).first()
        pace_record.pfitzinger = db.query(models.PfitzingerRaceTimePrediction).filter(
            models.PfitzingerRaceTimePrediction.pace_prediction_id == pace_record.id
        ).first()
        pace_record.matt_fitzgerald = db.query(models.MattFitzgeraldRaceTimePrediction).filter(
            models.MattFitzgeraldRaceTimePrediction.pace_prediction_id == pace_record.id
        ).first()

    return {"race_records": race_records, "pace_records": pace_records}


@router.get("/pace-records/{record_id}", response_model=schemas.PacePredictionBase)
def get_user_pace_record(record_id: int, db: Session = Depends(get_db)):
    pace_record = (
        db.query(models.PacePrediction)
        .options(
            joinedload(models.PacePrediction.daniels_old),
            joinedload(models.PacePrediction.daniels_new),
            joinedload(models.PacePrediction.pfitzinger),
            joinedload(models.PacePrediction.matt_fitzgerald),
        )
        .filter(models.PacePrediction.id == record_id)
        .first()
    )
    if pace_record is None:
        raise HTTPException(status_code=404, detail="Pace record not found")

    return pace_record


@router.get("/race-records/{record_id}", response_model=schemas.RaceTimePredictionBase)
def get_user_race_record(record_id: int, db: Session = Depends(get_db)):
    race_record = db.query(models.RaceTimePrediction).filter(models.RaceTimePrediction.id == record_id).first()
    if race_record is None:
        raise HTTPException(status_code=404, detail="Race record not found")

    return race_record