from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..hashing import Hash
from ..models import User

router = APIRouter(
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/user", response_model=schemas.UserDetails, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    # Check if the email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    try:
        # Hash the password
        hashed_password = Hash.bcrypt(user.password)
        # Create the user
        db_user = User(name=user.name, email=user.email, password=hashed_password)
        # Add the user to the database
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        # Return the user as a Pydantic model
        return db_user
    except Exception as e:
        # Handle database or other errors
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")


@router.get("/user/{user_id}", response_model=schemas.UserDetails)
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Return the user details as a Pydantic model
    return user

@router.post("/strava-user", response_model=schemas.StravaUserDetails)
def create_strava_user(user: schemas.StravaUser, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.strava_id == user.strava_id).first()
    if existing_user:
        return existing_user

    try:
        # Create the user
        db_user = User(name=user.name, strava_id=user.strava_id)
        # Add the user to the database
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User created successfully")
    except Exception as e:
        # Handle database or other errors
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")
    

@router.get("/strava-user/{strava_id}", response_model=schemas.StravaUserDetails)
def read_user(strava_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.strava_id == strava_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Return the user details as a Pydantic model
    return user