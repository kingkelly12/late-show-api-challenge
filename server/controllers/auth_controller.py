from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models.user import User  
from server import db  
from werkzeug import exceptions

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise exceptions.BadRequest('Username and password are required')

    if User.query.filter_by(username=username).first():
        raise exceptions.Conflict('Username already exists')

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise exceptions.BadRequest('Username and password are required')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        raise exceptions.Unauthorized('Invalid credentials')

    access_token = user.create_access_token()
    return jsonify({'access_token': access_token}), 200