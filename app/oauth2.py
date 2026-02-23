import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timezone,timedelta

SECRET_KEY = "e1d98cb602ff95af813b39b2ff54321a925e5e08c8a7ad0e463af0f2c6cc33b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
