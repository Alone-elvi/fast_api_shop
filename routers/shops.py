from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.shop import ShopCreate, ShopUpdate, ShopResponse
from crud.shop import create_shop, update_shop

router = APIRouter()


@router.post("/shops/", response_model=ShopResponse)
def create_new_shop(shop: ShopCreate, db: Session = Depends(get_db)):
    db_shop = create_shop(db, shop)
    return db_shop


@router.put("/shops/{shop_id}", response_model=ShopResponse)
def change_shop(shop_id: int, shop: ShopUpdate, db: Session = Depends(get_db)):
    db_shop = update_shop(db, shop_id, shop)
    return db_shop
