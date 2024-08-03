from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        shop_id=product.shop_id,
        category_id=product.category_id,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return db_product


def get_products(db: Session):
    return db.query(Product).all()


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description

    try:
        db.commit()
        db.refresh(db_product)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}
