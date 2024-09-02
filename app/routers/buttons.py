from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/buttons",
    tags=['Buttons']
)

@router.get('/basics')
def basic_btn(request: Request):
    return templates.TemplateResponse("buttons/basics.html", {"request": request})

@router.get('/buttons_1')
def buttons_1(request: Request):
    return templates.TemplateResponse("buttons/buttons_1.html", {"request": request})

@router.get('/buttons_2')
def buttons_2(request: Request):
    return templates.TemplateResponse("buttons/buttons_2.html", {"request": request})