#!/bin/bash

# Mise à jour système
apt-get update
apt-get upgrade -y

# Installer Node.js et PM2
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt-get install -y nodejs
npm install -g pm2

# Installer PostgreSQL
apt-get install -y postgresql postgresql-contrib

# Démarrer et activer PostgreSQL
systemctl start postgresql
systemctl enable postgresql

# Configurer la base
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'diouf';"
sudo -u postgres psql -c "CREATE DATABASE movies_db;"
sudo -u postgres psql -d movies_db -c "
  CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
  );"

# Installer Python et dépendances
apt-get install -y python3 python3-pip python3-venv
cd /vagrant/srcs/inventory-app
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Démarrer avec PM2
pm2 start server.py --name inventory_app --interpreter=venv/bin/python3
pm2 save
pm2 startup