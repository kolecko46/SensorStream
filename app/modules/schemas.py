from pydantic import BaseModel, EmailStr
from datetime import datetime


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

class Login(BaseModel):
    email: EmailStr
    password: str
