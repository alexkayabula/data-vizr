from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.orders.order_model import Order
from app.products.products_model import Product
from app.auth.auth_model import User
from app.auth.decorator import token_required
from app.orders.order_helper import validate_order
from app.database.database import Database
from app.database.order_db_queries import OrderDbQueries
from app.database.products_db_queries import ProductDbQueries



class OrderView(MethodView):
    decorators = [token_required]
    def post(self, current_user):
        """Create an order."""
        products_db = ProductDbQueries()
        order_db = OrderDbQueries()
        data = request.get_json()

        if validate_order(data) == 'valid':
            product_query = products_db.fetch_all_products()
            for product in product_query:
                if product['product_name'] == data['product_name']:
                    username =  current_user.username
                    order_db.insert_order_data(data, username)
                    response = {'message': 'Your order has been placed successfully.'}
                    return make_response(jsonify(response)), 201
            return jsonify({'message': 'Product not found.'})
        return jsonify({'message': validate_order(data)}), 406
