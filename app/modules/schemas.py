from pydantic import BaseModel
from datetime import datetime


class SensorData(BaseModel):
    temperature: str
    humidity: str
    date_time: str