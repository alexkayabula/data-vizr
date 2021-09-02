"""This module handles handles registering endponts"""
from flask import Blueprint
from app.auth.api import SignupView

AUTH_BLUEPRINT = Blueprint('auth', __name__)

# Define the API resource
SIGNUP_VIEW = SignupView.as_view('SIGNUP_VIEW')

# Add the url rule for signuping a user
AUTH_BLUEPRINT.add_url_rule(
    '/api/v2/auth/signup',
    view_func=SIGNUP_VIEW,
    methods=['POST'])
