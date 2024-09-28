from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class SensorData(BaseModel):
    temperature: str
    humidity: str
    created_at: datetime

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr

    class Config:
        orm_mode = True

class GetUser(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class LoginUser(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None