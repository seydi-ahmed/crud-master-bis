# crud-master/srcs/api-gateway/app/__init__.py

# Initialisation du module API Gateway
from flask import Flask
from .rabbitmq_client import publish_to_billing

app = Flask(__name__)

# Import des routes (évite les dépendances circulaires)
from . import main