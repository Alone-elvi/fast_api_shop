from services.rabbitmq import RabbitMQClient
from db import get_db
from sqlalchemy.orm import Session
from models.order import Order
from schemas.order import OrderCreate
import logging
import os

# Убедитесь, что папка для логов существует
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логгера
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(log_directory, "order_processor.log")),
        # logging.StreamHandler(),  # Для вывода логов в консоль
    ],
)

rabbitmq_client = RabbitMQClient()
rabbitmq_client.connect()
rabbitmq_client.declare_queue("processing_orders")
rabbitmq_client.declare_queue("notifications")


def process_order(message: dict):
    logging.debug("Received message: %s", message)
    db: Session = next(get_db())
    try:
        order_data = OrderCreate(**message)
        order_dict = order_data.model_dump(exclude_unset=True)
        new_order = Order(**order_dict)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        logging.debug("New order added: %s", new_order)

        new_order.status = "processed"
        db.commit()
        logging.debug("Order status updated: %s", new_order.status)

        # Отправка уведомления клиенту
        notification_message = {
            "user_id": new_order.user_id,
            "order_id": new_order.id,
            "status": new_order.status,
        }
        rabbitmq_client.publish("notifications", notification_message)
        logging.debug("Notification sent: %s", notification_message)
    except Exception as e:
        logging.error("Error processing order: %s", e)
    finally:
        db.close()
    print(f"Processed order: {new_order.id}")


def start_order_processor():
    logging.info("Starting order processor...")
    rabbitmq_client.consume("processing_orders", callback=process_order)
    logging.info("Started consuming...")
    rabbitmq_client.start_consuming()
    logging.info("Order processor is running...")
