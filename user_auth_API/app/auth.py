from app.db import (get_session, select_user_by_email)
from fastapi import Depends, HTTPException
from sqlmodel import Session
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from app.config import (ALGORITHM, SECRET_KEY)
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login/')

def get_current_user(session : Session = Depends(get_session), token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="invalid token")

    email = payload.get("sub")

    if email is None:
        raise HTTPException(status_code=401, detail= "invalid token")

    user = select_user_by_email(session,email)

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")


    return user
