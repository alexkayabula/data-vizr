"""This module handles user database queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from .database import Database

class UserDbQueries(Database):
    """This class handles database transactions for the user."""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_user_data(self, data):
        """Insert a new user record into the database."""
        query = "INSERT INTO users (name, username, password, admin_status)\
            VALUES('{}','{}', '{}', '{}');".format(data['name'],
                                             data['username'],
                                             generate_password_hash
                                             (data['password']), False)
        self.cur.execute(query)
        self.conn.commit()
