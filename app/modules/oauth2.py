from jose import JWTError, jwt
from datetime import datetime, timedelta, UTC
from . import credentials, schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = credentials.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode,
                             SECRET_KEY, 
                             ALGORITHM)
    
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])

        user_id: str = payload.get("user_id")

        if user_id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=user_id)
    
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate:": "Bearer"})
    
    return verify_access_token(token, credentials_exception)