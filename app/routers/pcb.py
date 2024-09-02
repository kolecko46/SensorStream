from fastapi import status, HTTPException, APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
       prefix="/pcb",
       tags=['Basic']
)

@router.get('/slave')
def scrt(request: Request):
    return templates.TemplateResponse("pcb/slave.html", {"request": request})

@router.get('/master')
def scrt(request: Request):
    return templates.TemplateResponse("pcb/master.html", {"request": request})