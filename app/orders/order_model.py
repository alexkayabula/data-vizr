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
    
    @classmethod
    def get_orders(cls, username):
        '''Retrieves a specific user's orders'''
        order_db = OrderDbQueries()
        orders = order_db.fetch_specific_order_by_parameter('orders', 'username', username)
        for order in orders:
            if order:
                return jsonify(orders), 200
        return jsonify({'message' : 'You have not made any orders'})
