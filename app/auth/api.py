from flask import current_app as app
from app.auth.auth_model import User
from app.auth.auth_helper import validate_signup, validate_login
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

class LoginView(MethodView):
    """Class-based view for user login and access token generation."""

    def post(self):
        '''Log in user and returns a token.'''
        database = Database(app.config['DATABASE_URL'])
        data = request.get_json()
        validate = validate_login(data)
        if validate == 'valid':
            try:
                query = database.fetch_by_parameter('users', 'username', data['username'])
                if not query:
                    response = {
                        'message': 'User not found ,' +
                        ' please register to continue.'
                    }
                    return make_response(jsonify(response)), 401
                the_user = User(query[0], query[1], query[2], query[3], query[4])
                
                if the_user.username == data['username'] and\
                        check_password_hash(the_user.password,
                                            data['password']):
                    # Generate the access token
                    token = jwt.encode(
                        {'username': the_user.username,
                         'exp': datetime.utcnow() +
                         timedelta(days=10, minutes=60)
                         }, 'donttouch')
                    if token:
                        response = {
                            'message': 'Login successful.',
                            'token': token.decode('UTF-8')
                        }
                        return make_response(jsonify(response)), 200
                else:
                    response = {
                        'message': 'Invalid password,' +
                        ' Please try again.'
                    }
                    return make_response(jsonify(response)), 403
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500
        return jsonify({'message': validate}), 406
