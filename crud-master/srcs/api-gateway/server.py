# crud-master/srcs/api-gateway/server.py

from flask import Flask, request, jsonify
from app.rabbitmq_client import publish_to_billing
import requests

app = Flask(__name__)

# Configuration des URLs des services
INVENTORY_API_URL = "http://192.168.56.20:8080/api/movies"

@app.route('/api/movies', methods=['GET', 'POST', 'DELETE'])
@app.route('/api/movies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def movies_gateway(id=None):
    # Route toutes les requêtes vers l'API Inventory
    if id:
        url = f"{INVENTORY_API_URL}/{id}"
    else:
        url = INVENTORY_API_URL
    
    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(),
        params=request.args
    )
    return jsonify(response.json()), response.status_code

@app.route('/api/billing', methods=['POST'])
def billing_gateway():
    # Publie les données dans RabbitMQ
    data = request.json
    publish_to_billing(data)
    return jsonify({"message": "Message posted to RabbitMQ"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)