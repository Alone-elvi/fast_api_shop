from sqlalchemy.orm import Session
from models.order import Order
from schemas.order import OrderCreate, OrderUpdate


def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        user_id=order.user_id, product_id=order.product_id, quantity=order.quantity
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order.id).first()
    db_order.user_id = order.user_id
    db_order.product_id = order.product_id
    db_order.quantity = order.quantity
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, id: int):
    db_order = db.query(Order).filter(Order.id == id).first()
    db.delete(db_order)
    db.commit()
