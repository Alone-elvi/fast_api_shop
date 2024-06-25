from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        shop_id=product.shop_id,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
