from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from modules.database_connector import connection, cursor
from modules import schemas, utilities
from modules import models
from modules.database_connector import engine, session_local, get_database

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['users']
)

@router.get("/test")
def test(db: Session = Depends(get_database)):
    return {"status":"ok"}

@router.get('/get_users')
def get_users(requuset: Request):
    sql = """SELECT * FROM moj_server.users"""
    cursor.execute(sql)

    users = cursor.fetchall()

    return{"data":users}

@router.get('/submit_user')
def get_form(request: Request):
    return templates.TemplateResponse("users/submit_user.html", {"request": request})

@router.post('/submit_user')
async def submit_form(request: Request, data:schemas.CreateUser):

    hashed_password = utilities.hash_password(data.password)

    sql = """INSERT INTO moj_server.users (first_name, last_name, password, email) VALUES (%s,%s,%s,%s)"""
    values = [data.first_name, data.last_name, hashed_password, data.email]

    cursor.execute(sql,values)

    connection.commit()

    return HTMLResponse(content=f"<p>hello {data.first_name}</p>")

@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("users/login.html", {"request": request})