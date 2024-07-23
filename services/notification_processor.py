from services.rabbitmq import RabbitMQClient

rabbitmq_client = RabbitMQClient()
rabbitmq_client.connect()
rabbitmq_client.declare_queue("notifications")

def send_notification(message: dict) -> None:
    user_id = message["user_id"]
    order_id = message["order_id"]
    status = message["status"]

    # Здесь можно добавить код для отправки уведомления (например, email или push-уведомление)
    print(f"Sending notification to user {user_id} about order {order_id}: {status}")

def start_notification_processor():
    rabbitmq_client.consume("notifications", callback=send_notification)
    print("Starting notification processor...")