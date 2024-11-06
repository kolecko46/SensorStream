from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from modules import oauth2

templates = Jinja2Templates(directory="templates")

router = APIRouter(
       tags=['Basic']
)

@router.get('/')
def root(request: Request):
    return templates.TemplateResponse("basics/root.html", {"request": request})

@router.get('/index')
def index(request: Request):
        #   user_id: int = Depends(oauth2.get_current_user)):
    
    return templates.TemplateResponse("basics/index.html", {"request": request})