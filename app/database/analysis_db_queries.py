"""This module handles product database queries."""
from urllib.parse import urlparse
import itertools
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from flask import jsonify
from .database import Database
from .order_db_queries import OrderDbQueries
from .products_db_queries import ProductDbQueries


class AnalysisDbQueries(OrderDbQueries, ProductDbQueries):
    """This class handles database transactions for the products."""

    def __init__(self):
        OrderDbQueries.__init__(self)
        ProductDbQueries.__init__(self)

    def fetch_all_prices_per_product(self):
        """Retrieve all price per product instances from the database."""
        products = ProductDbQueries().fetch_all_products()
        price_per_product_data = []
        for product in products:
            data = {product['product_name']: product['price']}
            price_per_product_data.append(data)
        return price_per_product_data
    
    def fetch_number_of_orders_per_product(self):
        """Retrieve number of orders per product from the database."""
        orders = OrderDbQueries().fetch_all_orders()
        orders_per_product = []
        keys = set()
        for order in orders:
            product_name = order['product_name']
            number_of_orders = order['quantity']
            data = {product_name: number_of_orders}
            if product_name not in keys:
                keys.add(product_name)
                orders_per_product.append(data)
            else:
                for data in orders_per_product:
                    for key, value in data.items():
                        if key == product_name:
                            number_of_orders = int (value) + int(number_of_orders)
                            data.update({product_name : number_of_orders})
        return orders_per_product
