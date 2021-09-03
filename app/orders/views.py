"""Handles adding endponts to the blueprints"""
from flask import Blueprint
from app.orders.api import OrderView, OrdersManagementView

ORDER_BLUEPRINT = Blueprint('order', __name__)
ORDER_VIEW = OrderView.as_view('ORDER_VIEW')
ORDERS_MANAGEMENT = OrdersManagementView.as_view('ORDERS_MANAGEMENT')
ORDER_BLUEPRINT.add_url_rule('/api/v2/users/orders', view_func=ORDER_VIEW, methods=['POST'])
ORDER_BLUEPRINT.add_url_rule('/api/v2/users/orders', view_func=ORDER_VIEW, methods=['GET'])
ORDER_BLUEPRINT.add_url_rule('/api/v2/orders/',defaults={'orderId' : None},view_func=ORDERS_MANAGEMENT, methods=['GET'])
ORDER_BLUEPRINT.add_url_rule('/api/v2/orders/<int:orderId>',view_func=ORDERS_MANAGEMENT, methods=['GET'])
ORDER_BLUEPRINT.add_url_rule('/api/v2/orders/<int:orderId>',view_func=ORDERS_MANAGEMENT, methods=['PUT'])
