from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from server.models.user import User  
from server import db  
from werkzeug import exceptions

bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@bp.route('', methods=['POST'])
@jwt_required()
def create():
    data = request.json
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        raise exceptions.BadRequest('Rating, guest_id, and episode_id are required')

    if not 1 <= rating <= 5:
        raise exceptions.BadRequest('Rating must be between 1 and 5')

    guest = Guest.query.get(guest_id)
    if not guest:
        raise exceptions.NotFound('Guest not found')

    episode = Episode.query.get(episode_id)
    if not episode:
        raise exceptions.NotFound('Episode not found')

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201