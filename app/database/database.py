"""This module handles database queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app


class Database:
    """This class handles all database related operations."""

    def __init__(self, database_url):
        """Initializes the connection url."""
        parsed_url = urlparse(database_url)
        d_b = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port

        self.conn = psycopg2.connect(
            database=d_b, user=username, password=password,
            host=hostname, port=port)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def trancate_table(self, table):
        """Trancates the table."""
        self.cur.execute("TRUNCATE TABLE {} RESTART IDENTITY".format(table))

    def create_tables(self):
        """Creates database tables."""
        create_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id SERIAL PRIMARY KEY, name text , username text UNIQUE, password text , admin_status boolean)"
        self.cur.execute(create_table)
        try:
           query = "INSERT INTO users (name, username, password, admin_status)\
           VALUES('{}','{}', '{}', '{}');".format('admin', 'admin', generate_password_hash('admin'), True)
           self.cur.execute(query)                      
        except ( Exception, psycopg2.DatabaseError):
            pass
        
        create_table = "CREATE TABLE IF NOT EXISTS orders\
        (orderId SERIAL PRIMARY KEY, product_name text,\
        quantity text, username text, status text)"
        self.cur.execute(create_table)


        create_table = "CREATE TABLE IF NOT EXISTS products\
        (product_id SERIAL PRIMARY KEY, product_name text, price\
        text, category text)"
        self.cur.execute(create_table)


    def fetch_by_parameter(self, table_name, column, param):
        """Retrieves a single parameter from a specific table and column."""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(table_name, column, param)
        self.cur.execute(query)
        row = self.cur.fetchone()
        return row
