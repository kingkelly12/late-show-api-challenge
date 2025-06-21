from server import db, bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def create_access_token(self):
        return create_access_token(identity=self.id, expires_delta=timedelta(days=1))

    def __repr__(self):
        return f'<User {self.username}>'