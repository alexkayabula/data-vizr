"""Handles adding endponts to the blueprints"""
from flask import Blueprint
from app.analysis.api import PricePerProductView, OrdersPerProductView, OrdersPerUserView

PRICE_PER_PRODUCT_BLUEPRINT = Blueprint('price_per_product', __name__)
PRICE_PER_PRODUCT_VIEW = PricePerProductView.as_view('PRICE_PER_PRODUCT_VIEW')
PRICE_PER_PRODUCT_BLUEPRINT.add_url_rule('/api/v2/price_per_product', view_func=PRICE_PER_PRODUCT_VIEW, methods=['GET'])

ORDERS_PER_PRODUCT_BLUEPRINT = Blueprint('orders_per_product', __name__)
ORDERS_PER_PRODUCT_VIEW = OrdersPerProductView.as_view('ORDERS_PER_PRODUCT_VIEW')
ORDERS_PER_PRODUCT_BLUEPRINT.add_url_rule('/api/v2/orders_per_product', view_func=ORDERS_PER_PRODUCT_VIEW, methods=['GET'])

ORDERS_PER_USER_BLUEPRINT = Blueprint('orders_per_user', __name__)
ORDERS_PER_USER_VIEW = OrdersPerUserView.as_view('ORDERS_PER_USER_VIEW')
ORDERS_PER_USER_BLUEPRINT.add_url_rule('/api/v2/orders_per_user', view_func=ORDERS_PER_USER_VIEW, methods=['GET'])
