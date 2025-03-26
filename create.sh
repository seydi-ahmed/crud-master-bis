#!/bin/bash

# Création de l'arborescence
mkdir -p crud-master/{scripts,srcs/{api-gateway/app,billing-app/app,inventory-app/app}}

# Fichiers racine
touch crud-master/README.md
touch crud-master/config.yaml
touch crud-master/Vagrantfile
touch crud-master/.env
touch crud-master/.gitignore

# Fichiers pour api-gateway
touch crud-master/srcs/api-gateway/{requirements.txt,server.py}
touch crud-master/srcs/api-gateway/app/{__init__.py,main.py,rabbitmq_client.py}

# Fichiers pour billing-app
touch crud-master/srcs/billing-app/{requirements.txt,server.py}
touch crud-master/srcs/billing-app/app/{__init__.py,main.py,database.py,rabbitmq_consumer.py}

# Fichiers pour inventory-app
touch crud-master/srcs/inventory-app/{requirements.txt,server.py}
touch crud-master/srcs/inventory-app/app/{__init__.py,main.py,database.py,models.py}

# Scripts d'installation
touch crud-master/scripts/{install_inventory.sh,install_billing.sh,install_gateway.sh,setup_databases.sh}

# Rendre le script exécutable
chmod +x crud-master/scripts/*.sh

echo "Structure de projet créée avec succès!"