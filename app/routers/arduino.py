from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from modules import schemas
from modules.database_connector import connection, cursor
from datetime import datetime

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/arduino",
    tags=['Text']
)

@router.get('/test')
def text_1(request: Request):
    return {"arduino":"hello"}

@router.get('/dht11')
def get_dht11_data(request: Request):
    data_list = {"data":[]}
    sql = """SELECT * FROM moj_server.dht11"""

    cursor.execute(sql)

    sql_data = cursor.fetchall()

    for data in sql_data:
        formatted_data = [
            data[0],
            data[1],
            data[2].isoformat()
        ]
        data_list["data"].append(formatted_data)

    return JSONResponse(content=data_list)

@router.post('/dht11')
def dht11_sensor(data: schemas.SensorData):
    
    sql = """INSERT INTO moj_server.dht11 (temperature, humidity, created_at) VALUES (%s,%s,%s)"""
    values = (data.temperature, data.humidity, data.date_time)
    
    cursor.execute(sql,values)

    connection.commit()

    temperature = data.temperature
    humidity = data.humidity
    date_time = data.date_time
    # print(f"temperature:", {temperature}, " humidity:", {humidity}, " datetime:", {date_time})
