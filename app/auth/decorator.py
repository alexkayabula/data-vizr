"""creates a token required decorator helps in securing endpoints"""
from functools import wraps
from flask import request, jsonify, current_app as app
import jwt
from app.auth.auth_model import User
from app.database.database import Database


def token_required(f):
    """This the fuction to be decorated"""
    @wraps(f)
    def decorated(*args, **kwargs):
        """Creates the decorator"""
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, 'donttouch')
            database = Database(app.config['DATABASE_URL'])
            query = database.fetch_by_parameter(
                'users', 'username', data['username'])
            current_user = User(query[0], query[1], query[2], query[3], query[4])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
