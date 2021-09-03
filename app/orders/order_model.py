from flask import Flask, jsonify, request, make_response, current_app as app
from app.products.products_model import Product
from app.auth.auth_model import User
from app.orders.order_helper import validate_order
from app.database.database import Database
from app.database.order_db_queries import OrderDbQueries
from app.database.products_db_queries import ProductDbQueries


class Order:
    def __init__(self, orderId, product_name, quantity, username, status):
        self.orderId = orderId
        self.product_name = product_name
        self.quantity = quantity
        self.username = username
        self.status = status
