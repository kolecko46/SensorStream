from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from modules import schemas, oauth2
from modules.models import Base, DHT11_data
from modules.database_connector import engine, get_database
from typing import List

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/arduino",
    tags=["Arduino"]
)
# DATA
@router.get('/dht11',
            response_model=List[schemas.SensorData])
def get_dht11_data(request: Request,
                   database: Session = Depends(get_database),
                   user_id: int = Depends(oauth2.get_current_user)):
    
    data = database.query(DHT11_data).all()

    return data

# DATA
@router.post('/dht11')
def dht11_sensor(data: schemas.SensorData,
                 database: Session = Depends(get_database)):
    
    new_data = DHT11_data(**data.dict()) 
    
    database.add(new_data)
    database.commit()
    database.refresh(new_data)