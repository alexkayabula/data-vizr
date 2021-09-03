"""This module handles order database queries."""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from .database import Database


class OrderDbQueries(Database):
    """This class handles database transactions orders."""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_order_data(self, data, username):
        """Insert a new order record into the database."""
        query = "INSERT INTO orders (product_name, quantity, username, status)\
        VALUES('{}', '{}', '{}', '{}');".format(data['product_name'], data['quantity'], username, 'new')
        self.cur.execute(query)
        self.conn.commit()
