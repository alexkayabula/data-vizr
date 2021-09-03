import unittest
import psycopg2
from flask import json
from app import create_app
from app.database.database import Database
from config import app_config


class TestBase(unittest.TestCase):
    """ Base class for all test classess """
    app = create_app('TESTING')
    app.app_context().push()
    client = app.test_client()

    user = {
        'name': ' joel',
        'username': 'joel',
        'password': 'password'
    }

    valid_admin_user = {
        'name': 'admin',
        'username': 'admin',
        'password': 'admin'
    }

    valid_non_admin_user = {
        'name': ' joel',
        'username': 'joel',
        'password': 'password'
    }

    valid_product = {
        'product_name': 'keyboard',
        'price': "3000",
        'category': "electronics"
    }

    invalid_order = {
            'product_name': '@#$%',
            'quantity': '@#$%',
        }

    valid_order = {
        'product_name': 'keyboard',
        'quantity': '3',
    }
    
    valid_update = {
        'status' : 'completed'
    }

    invalid_update = {
        'status' : ''
    }

    order_invalid_quantity = {
            'product_name': 'keyboard',
            'quantity': '@#',
        }

    order_empty_key ={
        '' : 'keyboard',
        'quantity' : '5'
    }

    def setUp(self):
        db = Database(app_config['TESTING'].DATABASE_URL)
        db.create_tables()
        self.create_valid_user()

    def create_valid_user(self):
        """ Registers a user to be used for tests"""
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(self.valid_admin_user),
                                    content_type='application/json')
        return response

    def get_admin_token(self):
        ''' Generates admin token to be used for tests'''
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.valid_admin_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        return data['token']
    
    def get_non_admin_token(self):
        ''' Generates a token to be used for tests'''
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.valid_non_admin_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        return data['token']
   
        def create_valid_product(self):
        """ Creates a valid product to be used for tests """
        response = self.client.post('api/v2/products',
                                    data=json.dumps(self.valid_product),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})

        def create_valid_order(self):
        """ Creates a valid order to be used for tests """
        response = self.client.post('api/v2/users/orders',
                                    data=json.dumps(self.valid_order),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        return response
         
                                             
    def tearDown(self):
        db = Database(app_config['TESTING'].DATABASE_URL)
        db.trancate_table("users")
        db.trancate_table("orders")
        db.trancate_table("products")
