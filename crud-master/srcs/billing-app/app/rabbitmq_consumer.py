# crud-master/srcs/billing-app/app/rabbitmq_consumer.py

import pika, json
from .database import db, Order

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='billing_queue', durable=True)

    def callback(ch, method, properties, body):
        data = json.loads(body)
        order = Order(
            user_id=data['user_id'],
            number_of_items=data['number_of_items'],
            total_amount=data['total_amount']
        )
        db.session.add(order)
        db.session.commit()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='billing_queue', on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()