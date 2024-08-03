from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.category import Category
from schemas.category import CategoryCreate

# from main import get_db


def get_categories(db: Session):
    return db.query(Category).all()


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db_category.name = category.name
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted"}
