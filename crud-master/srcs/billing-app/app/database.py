# crud-master/srcs/billing-app/app/database.py

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    number_of_items = db.Column(db.String(50), nullable=False)
    total_amount = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())