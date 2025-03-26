# crud-master/srcs/billing-app/app/main.py

from . import app, db
from .rabbitmq_consumer import consume
import threading

def run_consumer():
    """Lance le consumer RabbitMQ en arrière-plan"""
    print("🚀 Démarrage du consumer RabbitMQ...")
    consume()

# Démarrer le consumer au lancement
threading.Thread(target=run_consumer, daemon=True).start()
