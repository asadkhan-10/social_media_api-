import jwt
from jwt.exceptions import InvalidTokenError
from . import schemas
from fastapi import Depends,status, HTTPException
from datetime import datetime, timezone,timedelta
from fastapi.security import OAuth2PasswordBearer


oauth2_schema= OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "e1d98cb602ff95af813b39b2ff54321a925e5e08c8a7ad0e463af0f2c6cc33b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verfiy_access_token(token: str, credentials_exception):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id : str = payload.get("user_id")
        if not id:
            raise credentials_exception
        
        token_data= schemas.TokenData(id=id)
    except InvalidTokenError:
        raise credentials_exception
    return token_data
    
def get_current_user(token: str= Depends(oauth2_schema)):
    credentials_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not verify user credentials",headers={"WWW-Authenticate":"Bearer"})
    return verfiy_access_token(token, credentials_exception)
    
    
        