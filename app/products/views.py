"""Handles adding endponts to the blueprints"""
from flask import Blueprint
from app.products.api import ProductView

PRODUCTS_BLUEPRINT = Blueprint('products', __name__)
PRODUCTS_VIEW = ProductView.as_view('PRODUCTS_VIEW')
PRODUCTS_BLUEPRINT.add_url_rule('/api/v2/products', view_func=PRODUCTS_VIEW, methods=['POST'])
PRODUCTS_BLUEPRINT.add_url_rule('/api/v2/products', view_func=PRODUCTS_VIEW, methods=['GET'])
PRODUCTS_BLUEPRINT.add_url_rule('/api/v2/products/<int:product_id>', view_func=PRODUCTS_VIEW, methods=['PUT'])
