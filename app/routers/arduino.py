from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from modules import schemas
from modules.database_connector import connection, cursor
import pandas


templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/arduino",
    tags=['Arduino']
)

@router.get('/test')
def text_1(request: Request):
    return {"arduino":"hello"}

@router.get('/dht11')
def get_dht11_data(request: Request):
    data_frame = pandas.read_sql("SELECT * FROM moj_server.dht11", connection)
    html_table = data_frame.to_html(index=False)
    
    with open("./templates/arduino/dht11_data.html", "w") as file:
        file.write(html_table)

    return templates.TemplateResponse("arduino/dht11_data.html", {"request": request})

@router.post('/dht11')
def dht11_sensor(data: schemas.SensorData):
    
    sql = """INSERT INTO moj_server.dht11 (temperature, humidity, created_at) VALUES (%s,%s,%s)"""
    values = (data.temperature, data.humidity, data.date_time)
    
    cursor.execute(sql,values)

    connection.commit()