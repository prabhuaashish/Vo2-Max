from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..hashing import Hash
from ..models import User


router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    # Hash the password
    hashedPassword = Hash.bcrypt(user.password)
    # Create the user
    db_user = User(name=user.name, email=user.email, password=hashedPassword)
    # Add the user to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Return the user as a Pydantic model
    return db_user

@router.get("/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Return the user details as a Pydantic model
    return user