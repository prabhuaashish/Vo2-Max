from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas
from ..models import User
from ..hashing import Hash
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from ..token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
async def login(request: schemas.Login, response: JSONResponse, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    # generate a jwt token and set cookies

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    
    response.set_cookie(key="jwt_token", value=access_token, samesite="None", httponly=True, secure=True)
    response.set_cookie(key="user_id", value=user.id, samesite="None", httponly=True, secure=True)



    # return JSONResponse(content={"status": "ok"})
    return {"status": "ok"}