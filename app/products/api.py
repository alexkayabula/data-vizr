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
        decorators = [token_required]
        
    def get(self, current_user):
        """Return all products."""
        product = Product.get_all_products()
        return product

    decorators = [token_required]
    def put(self, current_user, product_id):
        """Update a product."""
        product_db = ProductDbQueries()
        data = request.get_json()
        if current_user.username == 'admin':
            query = product_db.fetch_by_parameter('products', 'product_id', product_id)
            if query:
                if validate_product(data) == "valid":
                    product_name = data['product_name']
                    price = data['price']
                    category = data['category']
                    product_db.update_product(product_name, price, category, product_id)
                    updated_product = product_db.fetch_specific_product_by_parameter('products', 'product_id', product_id)
                    return jsonify (updated_product)
                return jsonify({'message': validate_product(data)}), 406
            return jsonify ({'message' : "Product not found."})
        return jsonify({'message' : "You do not have admin rights."})
