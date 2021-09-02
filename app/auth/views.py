"""This module handles handles registering endponts"""
from flask import Blueprint
from app.auth.api import SignupView, LoginView

AUTH_BLUEPRINT = Blueprint('auth', __name__)

# Define the API resource
SIGNUP_VIEW = SignupView.as_view('SIGNUP_VIEW')
LOGIN_VIEW = LoginView.as_view('LOGIN_VIEW')

# Add the url rule for signuping a user
AUTH_BLUEPRINT.add_url_rule(
    '/api/v2/auth/signup',
    view_func=SIGNUP_VIEW,
    methods=['POST'])

AUTH_BLUEPRINT.add_url_rule(
    '/api/v2/auth/login',
    view_func=LOGIN_VIEW,
    methods=['POST']
)
