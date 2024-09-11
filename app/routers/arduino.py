from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from modules import schemas
from modules.models import Base, DHT11_data
from modules.database_connector import engine, connection, cursor, get_database
from typing import List

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/arduino",
    tags=['Arduino']
)

@router.get('/test')
def text_1(request: Request):
    return {"arduino":"hello"}

@router.get('/dht11', response_model=List[schemas.SensorData])
def get_dht11_data(request: Request, database: Session = Depends(get_database)):
    data_query = database.query(DHT11_data).all()

    return data_query

@router.post('/dht11')
def dht11_sensor(data: schemas.SensorData):
    
    sql = """INSERT INTO moj_server.dht11 (temperature, humidity, created_at) VALUES (%s,%s,%s)"""
    values = (data.temperature, data.humidity, data.date_time)
    
    cursor.execute(sql,values)

    connection.commit()


 