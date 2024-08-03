from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.category import CategoryCreate, CategoryShema, CategoriesResponse
from crud.category import create_category, get_categories, update_category, delete_category

router = APIRouter()


@router.post("/categories/", response_model=CategoryCreate)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_categories = create_category(db, category)
    return db_categories


@router.get("/categories/", response_model=list[CategoryShema])
def read_categories(db: Session = Depends(get_db)):
    db_categories = get_categories(db)
    return db_categories


@router.patch("/categories/{category_id}", response_model=CategoryShema)
def uopdate_categories(
    category_id: int, category: CategoryCreate, db: Session = Depends(get_db)
):
    db_categories = update_category(db, category_id, category)
    return db_categories


@router.delete("/categories/{category_id}")
def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_categories = delete_category(db, category_id)
    return db_categories