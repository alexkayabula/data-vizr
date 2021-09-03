from flask import json
from test_base import TestBase


class TestOrder(TestBase):
    """ Defines tests for the view methods of orders 
    """
    def test_posting_order_with_empty_keys(self):
        """ Creates an order with empty keys """
        response = self.client.post('api/v2/users/orders',
                                    data=json.dumps(self.order_empty_key),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('All keys are required.', str(response.data))

    def test_posting_an_order_with_invalid_or_expired_token(self):
        """ Tests accessing the orders endpoint with an invalid
        or expired token. """
        response = self.client.post('/api/v2/users/orders',
                                    headers={'Authorization':
                                             'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token is invalid', str(response.data))

    def test_create_an_order_for_non_product_item(self):
        """ Tests placing an order with for non existant product item. """
        response = self.create_valid_order()
        self.assertEqual(response.status_code, 200)
        self.assertIn('"message": "Product not found."', str(response.data))

    def test_create_order_with_invalid_characters(self):
        """ Tests creating a product with a invalid product_name or quantity. """
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(self.invalid_order),
                                    content_type='application/json',
                                    headers={'Authorization':
                                            self.get_admin_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_order_with_invalid_quantiy(self):
        """ Tests creating a product with a invalid product_name or quantity."""
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(
                                        self.order_invalid_quantity),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_admin_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('Quantity should be an integer.', str(response.data))

    def test_get_all_orders(self):
        """ Tests a users getting all their orders. """
        response = self.client.get('/api/v2/users/orders',
                                   headers={'Authorization':
                                            self.get_admin_token()})
        self.assertEqual(response.status_code, 200)

    def test_admin_get_specific_orders(self):
        """ Tests admin getting a specific order.  """
        self.create_valid_product()
        self.create_valid_order()
        response = self.client.get('/api/v2/orders/1',
                                   headers={'Authorization':
                                            self.get_admin_token()})
        self.assertEqual(response.status_code, 200)

    def test_non_admin_getting_an_order(self):
        """ Tests non admin getting an order. """
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(self.valid_non_admin_user),
                                    content_type='application/json')
        self.create_valid_product()
        self.create_valid_order()
        response = self.client.get('/api/v2/orders/1',
                                   data=json.dumps(self.valid_order),
                                   content_type='application/json',
                                   headers={'Authorization':
                                            self.get_non_admin_token()})
        self.assertIn('You do not have admin rights.', str(response.data))
        self.assertEqual(response.status_code, 200)
