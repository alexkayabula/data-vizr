from flask import jsonify, make_response
from app.database.database import Database
from app.database.products_db_queries import ProductDbQueries


class Product:
    def __init__(self,product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category
    
    def add_product(self, data):
        """Adds a product."""
        products_db = ProductDbQueries()
        product_query = products_db.fetch_all_products()
        for product in product_query:
            if product['product_name'] == data['product_name'] and \
                product['price'] == data['price'] and product['category'] == data['category']:
                response = {'message': 'This product already exists.'}
                return make_response(jsonify(response)), 409
        products_db.insert_product_data(data)
        response = {'message': 'Product added successfully.'}
        return make_response(jsonify(response)), 201
        
    @classmethod
    def get_all_products(cls):
        """Retrieves all products."""
        products_db = ProductDbQueries()
        products = products_db.fetch_all_products()
        if products == []:
            return jsonify(
                {"message": "There are no products at the moment."}), 200
        return jsonify(products), 200
      