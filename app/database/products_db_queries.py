"""This module handles product database queries."""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from .database import Database


class ProductDbQueries(Database):
    """This class handles database transactions for the products."""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_product_data(self, data):
        """Insert a new product into the database."""
        query = "INSERT INTO products (product_name, price, category)\
        VALUES('{}', '{}', '{}');".format(data['product_name'], data['price'], data['category'])
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all_products(self):
        """Retrieve all products from the database."""
        self.cur.execute("SELECT * FROM products ")
        rows = self.cur.fetchall()
        products = []
        for row in rows:
            row = {'product_id': row[0], 'product_name': row[1], 'price': row[2], 'category': row[3]}
            products.append(row)
        return products

    def fetch_specific_product_by_parameter(self, table_name, column, param):
        """Retrieve a single parameter from a specific table and column."""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(table_name, column, param)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        products = []
        for row in rows:
            row = {'product_id': row[0], 'product_name': row[1], 'price': row[2], 'category': row[3]}
            products.append(row)
        return products
    
    def update_product(self, product_name, price, category, product_id, ):
        query = "UPDATE products SET product_name = '{}', price = '{}', category = '{}' WHERE product_id = {}".format(product_name, price, category, product_id)
        self.cur.execute(query)
