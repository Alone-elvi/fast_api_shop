from sqlalchemy.orm import Session
from models.shop import Shop
from schemas.shop import ShopCreate

def create_shop(db: Session, shop: ShopCreate):
    db_shop = Shop(
        name=shop.name,
        owner_id=shop.owner_id
    )
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop
