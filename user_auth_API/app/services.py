
from app.db import select_user_by_email
from app.security import verify_password

def authenticate_user(session, email, password):
    user = select_user_by_email(session, email)

    if not user:
        return None
    
    if not verify_password(password, user.password_hash):  
        return None

    return user

#dev function only
def promote_to_admin(session, email: str):
    user = select_user_by_email(session, email)

    if not user:
        return None

    user.role = "admin"

    session.commit()
    session.refresh(user)

    return user