from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas
from ..models import User
from ..hashing import Hash
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from ..token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=schemas.UserResponse)
async def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    # generate a jwt token and return it

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    # Include the user information in the response
    response_data = {
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "access_token": access_token,
        "token_type": "bearer",
    }

    return response_data