import unittest
from flask import json
import psycopg2
from test_base import TestBase


class TestAuth(TestBase):

    def test_register_valid_details(self):
        """ Tests creating a new user with valid details """
        test_user = {
            'name': 'test',
            'username': 'username',
            'password': 'password'
        }
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(test_user),
                                    content_type='application/json')
        self.assertIn('You registered successfully. Please login.',
                      str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_register_with_invalid_characters(self):
        """ Tests creating a new user with invalid characters """
        inv_char = {
            'name': 'alex',
            'username': '#$%',
            'password': '@#$%'
        }
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(inv_char),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn("The username should only contain alphabetic characters.", str(response.data))

    def test_register_with_blank_inputs(self):
        """ Tests creating a new user with blank """
        inv_char = {
            'name': '',
            'username': ' ',
            'password': ''
        }
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(inv_char),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn("All fields are required.", str(response.data))

    def test_register_with_empty_keys(self):
        """ Tests registering a new user with empty keys """
        empty_key = {
            '': 'alex',
            'username': 'alex',
            'password': 'alex'
        }
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(empty_key),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn("All keys are required.", str(response.data))

    def test_register_non_json_input(self):
        """ Tests register with non valid JSON input """
        response = self.client.post('/api/v2/auth/signup',
                                    data='some non json data',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('"message": "Please check your inputs, inputs should be in JSON format"' , str(response.data))

    def test_register_existing_user(self):
        """ Tests creating a new user with existing username """
        self.create_valid_user()
        response = self.create_valid_user()
        self.assertEqual(response.status_code, 409)
        self.assertIn("User already exists. Please login.", str(response.data))

    def test_register_invalid_json(self):
        """ Test register with invalid json """
        invalid_json = {
            'name' : 0.1,
            'username': 5,
            'password': 7
        }
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(invalid_json),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn('Invalid entry, Input should be in a valid json format.', str(response.data))
    
    def test_login_valid_credentials(self):
        """ Tests login with valid credentials """
        self.create_valid_user()
        user = {
            'username': 'admin',  # credentials for valid user.
            'password': 'admin'
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(user),
                                    content_type='application/json')
        self.assertIn('Login successful.', str(response.data))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertTrue(data['token'])

    def test_login_invalid_characters(self):
        """ Test login with invalid characters """
        inv_char = {
            'username': '#$%',
            'password': '@#$%'
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(inv_char),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)

    def test_login_invalid_json(self):
        """ Test login with invalid json """
        invalid_json = {
            'username': 5,
            'password': 7
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(invalid_json),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn('Invalid entry, Input should be in a valid json format.', str(response.data))

    def test_login_with_blank_inputs(self):
        """ Tests logging in a user with blank inputs """
        blank_inputs = {

            'username': ' ',
            'password': ''
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(blank_inputs),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)

    def test_login_with_empty_keys(self):
        """ Tests logging in with empty keys """
        empty_key = {

            '': 'admin',
            'password': 'admin'
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(empty_key),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 406)
        self.assertIn('All keys are required.', str(response.data))

    
    def test_login_wrong_password(self):
        """ Tests login with wrong password """
        user = {
            'name': 'admin',
            'username': 'admin',
            'password': 'admin'
        }
        self.client.post('/api/v2/auth/signup',
                         data=json.dumps(user),
                         content_type='application/json')
        user_login = {
            'username': 'admin',
            'password': '1234'
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(user_login),
                                    content_type='application/json')
        self.assertIn('"message": "Invalid password, Please try again."', str(response.data))
        self.assertEqual(response.status_code, 403)

    def test_login_wrong_username(self):
        """ Tests login with wrong username credentials """
        user = {
            'name': 'admin',
            'username': 'admin',
            'password': 'admin'
        }
        self.client.post('/api/v2/auth/signup',
                         data=json.dumps(user),
                         content_type='application/json')
        user_login = {
            'username': 'wrongusername',
            'password': 'admin'
        }
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(user_login),
                                    content_type='application/json')

        self.assertIn('User not found , please register to continue', str(response.data))
        self.assertEqual(response.status_code, 401)
