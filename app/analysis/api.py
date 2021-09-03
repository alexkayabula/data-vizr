from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.analysis.analysis_models import Analysis
from app.auth.decorator import token_required
from app.database.database import Database


class PricePerProductView(MethodView):
    
    decorators = [token_required]
    def get(self, current_user):
        """Return price per product dataset."""
        if current_user.username == "admin":
            price_per_product_dataset = Analysis.get_all_prices_per_product()
            return price_per_product_dataset
        return jsonify({'message' : "You do not have admin rights."})

class OrdersPerProductView(MethodView):

    decorators = [token_required]
    def get(self, current_user):
        """Return number of orders per product dataset."""
        if current_user.username == "admin":
            number_of_orders_per_product_dataset = Analysis.get_all_number_of_orders_per_product()
            return number_of_orders_per_product_dataset
        return jsonify({'message' : "You do not have admin rights."})

class OrdersPerUserView(MethodView):

    decorators = [token_required]
    def get(self, current_user):
        """Return number of orders per user dataset."""
        if current_user.username == "admin":
            number_of_orders_per_user_dataset = Analysis.get_all_number_of_orders_per_user()
            return number_of_orders_per_user_dataset
        return jsonify({'message' : "You do not have admin rights."})
