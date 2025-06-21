from flask import Blueprint, jsonify
from models import Guest
from werkzeug import exceptions

bp = Blueprint('guests', __name__, url_prefix='/guests')

@bp.route('', methods=['GET'])
def index():
    guests = Guest.query.all()
    data = [{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests]
    return jsonify(data), 200