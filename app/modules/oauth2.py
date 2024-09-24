from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "6f102a47cca91fba6316a778f16ff61e47d1bde050356b09ada5ca91b7260e53"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode,
                             SECRET_KEY, 
                             ALGORITHM)
    
    return encoded_jwt