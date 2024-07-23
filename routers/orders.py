from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.order import OrderCreate, OrderUpdate
from services.rabbitmq import RabbitMQClient

router = APIRouter()
rabbitmq_client = RabbitMQClient()
rabbitmq_client.connect()
rabbitmq_client.declare_queue("new_orders")


@router.post("/orders/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    order_data = order.model_dump(exclude_unset=True)
    rabbitmq_client.publish("new_orders", order_data)
    return {"message": "Order received and is being processed"}


@router.patch("/orders/{order_id}", response_model=OrderUpdate)
def update_order(order: OrderUpdate, db: Session = Depends(get_db)):
    order_data = order.model_dump(exclude_unset=True)
    rabbitmq_client.publish("orders", order_data)
    return {"message": "Order update received and is being processed"}
