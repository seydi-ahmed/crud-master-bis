# crud-master

## structure du projet
```
crud-master/
├── .env
├── .gitignore
├── README.md
├── Vagrantfile
├── config.yaml
├── scripts/
│   ├── install_billing.sh
│   ├── install_gateway.sh
│   ├── install_inventory.sh
│   └── setup_databases.sh
└── srcs/
    ├── api-gateway/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── main.py
    │   │   └── rabbitmq_client.py
    │   ├── requirements.txt
    │   └── server.py
    ├── billing-app/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── database.py
    │   │   ├── main.py
    │   │   └── rabbitmq_consumer.py
    │   ├── requirements.txt
    │   └── server.py
    └── inventory-app/
        ├── app/
        │   ├── __init__.py
        │   ├── database.py
        │   ├── main.py
        │   └── models.py
        ├── requirements.txt
        └── server.py
```

## commandes utiles
1) Arrêter les VMs si elles sont en marche
- vagrant halt
2) Relancer le provisionnement
- vagrant up --provision
3) Détruire les machines et relancer
- vagrant destroy -f && vagrant up
4) Dans Gateway, Dans Inventory, Dans Billing
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
5) Installer net-tools
- sudo apt install net-tools
6) Requierement
```
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
7) Dans inventory
- pip install psycopg2-binary
8) Supprimer le cache python
```
find . -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
```