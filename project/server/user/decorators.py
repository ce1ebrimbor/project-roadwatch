# project/server/user/views.py
from functools import wraps
from flask import request, jsonify, current_app
from project.server.models import User
import jwt
import datetime

def token_required(f):
    """
    Checks if the token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'})
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.get(data['id'])
        except:
            return jsonify({'message': 'Token is invalid'})

        return f(*args, **kwargs)
    return decorated