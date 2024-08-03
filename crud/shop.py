from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.shop import Shop
from schemas.shop import ShopCreate, ShopUpdate


def create_shop(db: Session, shop: ShopCreate):
    db_shop = Shop(name=shop.name, owner_id=shop.owner_id)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop


def update_shop(db: Session, shop_id: int, shop: ShopUpdate):
    db_shop = db.query(Shop).filter(Shop.id == shop_id).first()

    if not db_shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    if shop.name is not None:
        db_shop.name = shop.name
    if shop.owner_id is not None:
        db_shop.owner_id = shop.owner_id

    try:
        db.commit()
        db.refresh(db_shop)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

    return db_shop


def get_shop(db: Session, shop_id: int):
    db_shop = db.query(Shop).filter(Shop.id == shop_id).first()

    if not db_shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    
    return db_shop


def delete_shop(db: Session, shop_id: int):
    db_shop = db.query(Shop).filter(Shop.id == shop_id).first()

    if not db_shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    db.delete(db_shop)
    db.commit()
    return {"message": "Shop deleted"}