from flask import json
from test_base import TestBase


class TestProduct(TestBase):
    """ Defines tests for the view methods of product """
    def test_create_product_with_valid_details(self):
        """ Tests adding a product with valid details """
        response = self.create_valid_product()
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully.',str(response.data))

    def test_create_product_with_blank_attributes(self):
        """ Tests creating a product with a blank item name or price """
        product = {
            'product_name': '',
            'price': '',
            'category': ''
        }
        response = self.client.post('/api/v2/products',
                                    data=json.dumps(product),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_product_with_invalid_characters(self):
        """ Tests creating a product item with invalid item name or price """
        product = {
            'product_name': '@#$%',
            'price': '@#$%',
            'category': '@#$%'
        }
        response = self.client.post('/api/v2/products',
                                    data=json.dumps(product),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_product_with_invalid_price(self):
        """ Tests creating a product item with invalid price """
        product = {
            'product_name': 'keyboard',
            'price': '@#$%',
            'category': 'electronics'
        }
        response = self.client.post('/api/v2/products',
                                    data=json.dumps(product),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('The price should only contain numeric characters.', str(response.data))

    def test_create_product_with_invalid_json(self):
        """ Tests creating a product item with invalid json """
        product = {
            'product_name': 8,
            'price': 0.1,
            'category': 9
        }
        response = self.client.post('/api/v2/products',
                                    data=json.dumps(product),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('Invalid entry, Input should be in a valid json format.', str(response.data))
        
    def test_create_duplicate_product(self):
        """ Tests creating a duplicate product(same attributes) """
        self.create_valid_product()
        response = self.create_valid_product()
        self.assertEqual(response.status_code, 409)
    
    def test_get_product(self):
        """ Tests fetching all product """
        self.create_valid_product()
        response = self.client.get('/api/v2/products',
                                   headers={'Authorization':
                                            self.get_admin_token()})
        self.assertEqual(response.status_code, 200)

    def test_accessing_product_view_without_token(self):
        """ Tests accessing the product endpoint without a token """
        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 401)

    def test_accessing_product_view_with_invalid_or_expired_token(self):
        """ Tests accessing the product endpoint with an invalid
        or expired token """
        response = self.client.get('/api/v2/products',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)
