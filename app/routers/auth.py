from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from modules import schemas, utilities, models, oauth2
from modules.database_connector import engine, get_database

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix = "/login",
    tags = ["Authentication"]
)

# Login
# HTML
@router.get("")
def login_html(request: Request):
    
    return templates.TemplateResponse("users/login.html", {"request": request})

@router.post("")
def login(request: Request,
          data: OAuth2PasswordRequestForm = Depends(),
          database: Session = Depends(get_database)):
    
    user = database.query(models.Users).filter(models.Users.email == data.username).first()


    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid credentials")
    
    if not utilities.verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid credentials")
    
    # Create token
    acces_token = oauth2.create_access_token({"user_id":user.id})

    # Return token
    return JSONResponse(content={"access_token": acces_token, "token_type": "bearer"})