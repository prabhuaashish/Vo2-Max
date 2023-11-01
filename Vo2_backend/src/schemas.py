from pydantic import BaseModel


class CreateUserInput(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True