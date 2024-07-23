from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas.user import UserCreate, UserUpdate
from crud.user import create_user, update_user
from models.user import User


router = APIRouter()


@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/users/", response_model=UserCreate)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@router.put("/users/{user_id}", response_model=UserUpdate)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        db_user = update_user(db, user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return db_user
