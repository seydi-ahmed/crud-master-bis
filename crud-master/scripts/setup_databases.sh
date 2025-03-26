#!/bin/bash

apt-get update
apt-get install -y postgresql postgresql-contrib
service postgresql start

sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'diouf';"
sudo -u postgres psql -c "CREATE DATABASE movies_db;"
sudo -u postgres psql -c "CREATE DATABASE billing_db;"

# Setup inventory DB
sudo -u postgres psql -d movies_db -c "
  CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
  );"

# Setup billing DB
sudo -u postgres psql -d billing_db -c "
  CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    number_of_items VARCHAR(50) NOT NULL,
    total_amount VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );"