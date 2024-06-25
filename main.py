from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db

from schemas.user import UserCreate, UserUpdate
from schemas.category import CategoryCreate
from schemas.product import ProductCreate
from schemas.shop import ShopCreate

from crud.user import create_user, update_user
from crud.category import create_category
from crud.product import create_product
from crud.shop import create_shop


from models.user import User


app = FastAPI()


@app.get("/")
def home():
    return {"message": "First FastAPI app"}


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.post("/users/", response_model=UserCreate)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@app.put("/users/{user_id}", response_model=UserUpdate)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        db_user = update_user(db, user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return db_user


@app.post("/shops/", response_model=ShopCreate)
def create_new_shop(shop: ShopCreate, db: Session = Depends(get_db)):
    db_shop = create_shop(db, shop)
    return db_shop


@app.post("/products/", response_model=ProductCreate)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product)
    return db_product


@app.post("/categories/", response_model=CategoryCreate)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = create_category(db, category)
    return db_category
