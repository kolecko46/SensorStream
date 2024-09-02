from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from modules.database_connector import connection, cursor


templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['Searher']
)

@router.get('/searcher')
def text_1(request: Request):
    return templates.TemplateResponse("searcher/searcher.html", {"request": request})

@router.get('/excercise_1')
def text_1(request: Request):
    return templates.TemplateResponse("searcher/excercise_1.html", {"request": request})

@router.get('/submit')
def get_form(request: Request):
    return templates.TemplateResponse("searcher/submit.html", {"request": request})

@router.post('/submit')
def submit_form(request: Request,
                first_name:str = Form(...),
                last_name:str = Form(...),
                email:str = Form(...)):
    
    sql = """INSERT INTO moj_server.users (first_name, last_name, email) VALUES (%s,%s,%s)"""
    values = (first_name, last_name, email)

    cursor.execute(sql,values)

    connection.commit()

    print(f"First name {first_name}, last name {last_name}, email {email}")
    # return templates.TemplateResponse("searcher/searcher.html", {"request": request})
    return HTMLResponse(content=f"<p>hello {first_name}</p>")