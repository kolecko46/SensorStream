from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from modules import schemas, utilities, models, oauth2
from modules.database_connector import engine, get_database

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['users']
)

# Create user
# HTML
@router.get('/submit_user')
def get_form(request: Request):
    
    return templates.TemplateResponse("users/submit_user.html", {"request": request})

# DATA
@router.post('/submit_user',
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.GetUser)
async def create_user(data:schemas.CreateUser,
                      database: Session = Depends(get_database)):

    # Password hash
    hashed_password = utilities.hash_password(data.password)

    new_user = models.Users(first_name=data.first_name,
                            last_name=data.last_name,
                            password=hashed_password,
                            email=data.email)

    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    return HTMLResponse(content=f"<p>hello {data.first_name}</p>")

# Get all users
# DATA
@router.get('/get_users')
def get_users(request: Request,
              database: Session = Depends(get_database),
              user_id = Depends(oauth2.get_current_user)):
    
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token")

    users = database.query(models.Users).all()

    return{"data":users}


# Get user by ID
# DATA
@router.get('/users/{user_id}',
            response_model=schemas.GetUser)
def get_user(user_id: int,
             database: Session = Depends(get_database)):
    
    user = database.query(models.Users).filter(models.Users.id==user_id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")

    return user