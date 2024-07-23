from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.category import CategoryCreate
from crud.category import create_category

router = APIRouter()

@router.post("/categories/", response_model=CategoryCreate)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = create_category(db, category)
    return db_category
