from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from modules.database_connector import connection, cursor
from modules import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['Login']
)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), data = schemas.Login):
    sql = """SELECT * FROM moj_server.users"""