#!/bin/bash

# Mise à jour système
apt-get update
apt-get upgrade -y

# Installer Node.js et PM2
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt-get install -y nodejs
npm install -g pm2

# Installer PostgreSQL et RabbitMQ
apt-get install -y postgresql postgresql-contrib rabbitmq-server

# Démarrer et activer les services
systemctl start postgresql
systemctl enable postgresql
systemctl start rabbitmq-server
systemctl enable rabbitmq-server

# Configurer PostgreSQL
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'diouf';"
sudo -u postgres psql -c "CREATE DATABASE billing_db;"
sudo -u postgres psql -d billing_db -c "
  CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    number_of_items VARCHAR(50) NOT NULL,
    total_amount VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );"

# Configurer RabbitMQ
rabbitmqctl add_user guest guest
rabbitmqctl set_permissions -p / guest ".*" ".*" ".*"
rabbitmqctl declare queue billing_queue durable=true

# Installer Python et dépendances
apt-get install -y python3 python3-pip python3-venv
cd /vagrant/srcs/billing-app
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Démarrer avec PM2
pm2 start server.py --name billing_app --interpreter=venv/bin/python3
pm2 save
pm2 startup