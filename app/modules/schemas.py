from pydantic import BaseModel, EmailStr
from datetime import datetime


class SensorData(BaseModel):
    temperature: str
    humidity: str
    date_time: str

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr