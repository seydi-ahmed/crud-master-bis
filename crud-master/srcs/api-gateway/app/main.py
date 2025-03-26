# crud-master/srcs/api-gateway/app/main.py

from . import app
import requests
from flask import request, jsonify
from .rabbitmq_client import publish_to_billing

# Configuration des microservices
INVENTORY_SERVICE_URL = "http://192.168.56.20:8080"

@app.route('/api/movies', methods=['GET', 'POST', 'DELETE'])
@app.route('/api/movies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def movies_proxy(id=None):
    """Route les requêtes vers l'API Inventory"""
    url = f"{INVENTORY_SERVICE_URL}/api/movies/{id}" if id else f"{INVENTORY_SERVICE_URL}/api/movies"
    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(),
        params=request.args
    )
    return response.json(), response.status_code

@app.route('/api/billing', methods=['POST'])
def billing_proxy():
    """Publie les commandes dans RabbitMQ"""
    publish_to_billing(request.json)
    return {"message": "Message envoyé à la file d'attente"}, 200