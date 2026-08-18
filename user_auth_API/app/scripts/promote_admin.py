from app.db import engine
from app.services import promote_to_admin
from sqlmodel import Session

email = input("Type email: ").strip().lower()

with Session(engine) as session:
    user = promote_to_admin(session, email)

    if user:
        print(f"{user.email} is now admin.")
    else:
        print("User not found.")