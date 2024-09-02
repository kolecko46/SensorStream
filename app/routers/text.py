from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/text",
    tags=['Text']
)

@router.get('/text_1')
def text_1(request: Request):
    return templates.TemplateResponse("text/text_1.html", {"request": request})

@router.get('/text_2')
def text_2(request: Request):
    return templates.TemplateResponse("text/text_2.html", {"request": request})
