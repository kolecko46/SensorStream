from fastapi import status, HTTPException, APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
       tags=['Basic']
)

@router.get('/')
def root(request: Request):
    return templates.TemplateResponse("basics/root.html", {"request": request})

@router.get('/index')
def index(request: Request):
    return templates.TemplateResponse("basics/index.html", {"request": request})