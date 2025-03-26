# crud-master/srcs/billing-app/server.py

from app import create_app
from app.database import db, Order
from app.rabbitmq_consumer import consume
import threading

app = create_app()

def start_consumer():
    with app.app_context():  # Important pour le contexte Flask
        consume()

if __name__ == '__main__':
    # Démarrer le consumer dans un thread séparé
    consumer_thread = threading.Thread(target=start_consumer, daemon=True)
    consumer_thread.start()
    
    # Maintenir le script actif
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down...")