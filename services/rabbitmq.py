import pika
import json
from config import settings


class RabbitMQClient:
    def __init__(self):
        self.url = f"amqp://guest:guest@{settings.rabbitmq_host}:{settings.rabbitmq_management_port}/"
        self.host = settings.rabbitmq_host
        self.queue = settings.rabbitmq_queue
        self.port = settings.rabbitmq_port
        self.management_port = settings.rabbitmq_management_port
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)

    def publish(self, queue_name, message):
        self.channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
            ),
        )

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name, durable=True)

    def consume(self, queue_name, callback):
        def on_message(channel, method, properties, body):
            message = json.loads(body)
            callback(message)
            channel.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue_name, on_message_callback=on_message)

    def start_consuming(self):
        self.channel.start_consuming()

    def close(self):
        if self.connection:
            self.connection.close()
