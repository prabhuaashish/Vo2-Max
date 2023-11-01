from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import bcrypt

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True) 
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))


