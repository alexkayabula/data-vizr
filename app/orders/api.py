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

        def get(self, current_user):
            """Return single user orders."""
            username = current_user.username
            orders = Order.get_orders(username)
            return orders
        
class OrdersManagementView(MethodView):

    decorators = [token_required]
    def get(self, current_user, orderId):
        """Return all orders."""
        order_db = OrderDbQueries()
        if current_user.username == 'admin':
            if orderId:
                query = order_db.fetch_specific_order_by_parameter('orders', 'orderId', orderId)
                for order in query:
                    return jsonify({"orders" : order}), 200
                return jsonify({'message': "Order not found."}), 404
            all_orders = Order.get_all_orders()
            return all_orders
        return jsonify({'message' : "You do not have admin rights."})
