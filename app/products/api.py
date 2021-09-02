from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.products.products_model import Product
from app.auth.decorator import token_required
from app.products.products_helper import validate_product
from app.database.database import Database
from app.database.products_db_queries import ProductDbQueries


class ProductView(MethodView):
    decorators = [token_required]
    def post(self, current_user):
        """Create a new product."""
        data = request.get_json()
        if current_user.username == 'admin':
            if validate_product(data) == 'valid':
                #the trick
                product = Product(data['product_name'], data['price'], data['category'])
                return product.add_product(data)
            return jsonify({'message': validate_product(data)}), 406
        return jsonify({'message' : "You do not have admin rights"})
    