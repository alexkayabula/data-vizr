from flask import jsonify, make_response
from app.database.database import Database
from app.database.analysis_db_queries import AnalysisDbQueries


class Analysis:

        
    def get_all_prices_per_product():
        """Generate a prices per product dataset."""
        analysis_db = AnalysisDbQueries()
        price_per_product_dataset = analysis_db.fetch_all_prices_per_product()
        if price_per_product_dataset == []:
            return jsonify(
                {"message": "There is no data in the <prices_per_product_dataset>."}), 200
        return jsonify(price_per_product_dataset), 200
    
    def get_all_number_of_orders_per_product():
        """Generate an orders per product dataset."""
        analysis_db = AnalysisDbQueries()
        orders_per_product_dataset = analysis_db.fetch_number_of_orders_per_product()
        if orders_per_product_dataset == []:
            return jsonify(
                {"message": "There is no data in the <number_of_orders_per_product_dataset>."}), 200
        return jsonify(orders_per_product_dataset), 200

    def get_all_number_of_orders_per_user():
        """Generate an orders per user dataset."""
        analysis_db = AnalysisDbQueries()
        number_of_orders_per_user_dataset = analysis_db.fetch_number_of_orders_per_user()
        if number_of_orders_per_user_dataset == []:
            return jsonify(
                {"message": "There is no data in the <number_of_oders_per_user_dataset>."}), 200
        return jsonify(number_of_orders_per_user_dataset), 200
