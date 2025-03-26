#!/bin/bash

# Mise à jour système
apt-get update
apt-get upgrade -y

# Installer Node.js et PM2
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt-get install -y nodejs
npm install -g pm2

# Installer Python et dépendances
apt-get install -y python3 python3-pip python3-venv
cd /vagrant/srcs/api-gateway
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Démarrer avec PM2
pm2 start server.py --name gateway_app --interpreter=venv/bin/python3
pm2 save
pm2 startup