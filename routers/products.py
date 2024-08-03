from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.product import ProductCreate, Product
from crud.product import create_product, get_products

router = APIRouter()


@router.post("/products/", response_model=ProductCreate)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product)
    return db_product


@router.get("/products/", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    db_products = get_products(db)
    return db_products
