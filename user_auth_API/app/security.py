from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from app.config import (ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM, SECRET_KEY)
import jwt

password_hash=PasswordHash.recommended()

def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str):

    return password_hash.verify(password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})

    enconded_jwt = jwt.encode(payload=to_encode,key=SECRET_KEY,algorithm=ALGORITHM)

    return enconded_jwt
