from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Episode, Appearance
from werkzeug import exceptions

bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@bp.route('', methods=['GET'])
def index():
    episodes = Episode.query.all()
    data = [{'id': e.id, 'date': e.date.isoformat(), 'number': e.number} for e in episodes]
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['GET'])
def show(id):
    episode = Episode.query.get(id)
    if not episode:
        raise exceptions.NotFound('Episode not found')

    appearances = [{
        'id': a.id,
        'rating': a.rating,
        'guest': {
            'id': a.guest.id,
            'name': a.guest.name,
            'occupation': a.guest.occupation
        }
    } for a in episode.appearances]

    data = {
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def destroy(id):
    episode = Episode.query.get(id)
    if not episode:
        raise exceptions.NotFound('Episode not found')

    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200