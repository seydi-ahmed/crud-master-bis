import pika
import json

def publish_to_billing(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='billing_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='billing_queue',
        body=json.dumps(data),
        properties=pika.BasicProperties(delivery_mode=2)  # Persistent message
    )
    connection.close()