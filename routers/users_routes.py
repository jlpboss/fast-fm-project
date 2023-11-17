from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.import_schemas import User_Schema
from models.import_modles import User_Model
from controllers.user_controller import create_user, get_users
from database import SessionLocal

router = APIRouter(
    prefix="/user"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=User_Schema)
def Create_User(*, db: Session = Depends(get_db), user_in: User_Schema):
    new_user = create_user(db, user_in)
    return new_user

@router.get("/all", response_model=List[User_Schema])
def get_items(db: Session = Depends(get_db)):
    items = get_users(db)
    return items