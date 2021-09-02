from flask import current_app as app
from app.auth.auth_model import User
from app.auth.auth_helper import validate_signup
from app.database.database import Database
from app.database.user_db_queries import UserDbQueries


class SignupView(MethodView):
    """Class-based view registers a new user."""

    def post(self):
        """Signs up a user."""
        database = Database(app.config['DATABASE_URL'])
        user_db = UserDbQueries()
        data = request.get_json()
        validate = validate_signup(data)
        if validate == 'valid':
            user_query = database.fetch_by_parameter(
                'users', 'username', data['username'])
            if user_query:
                response = {'message': 'User already exists. Please login.'}
                return make_response(jsonify(response)), 409
            else:
                user_db.insert_user_data(data)
                response = {'message': 'You registered successfully. Please login.'}
                return make_response(jsonify(response)), 201
        return jsonify({'message': validate}), 406
