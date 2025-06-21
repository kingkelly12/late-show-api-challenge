from server import app, db
from models import User, Guest, Episode, Appearance
from datetime import date

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create test user
        user = User(username='test', password='test123')
        db.session.add(user)

        # Create guests
        guests = [
            Guest(name='John Doe', occupation='Actor'),
            Guest(name='Jane Smith', occupation='Musician'),
            Guest(name='Bob Johnson', occupation='Comedian')
        ]
        db.session.add_all(guests)

        # Create episodes
        episodes = [
            Episode(date=date(2023, 1, 1), number=101),
            Episode(date=date(2023, 1, 2), number=102),
            Episode(date=date(2023, 1, 3), number=103)
        ]
        db.session.add_all(episodes)

        # Create appearances
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2),
            Appearance(rating=2, guest_id=1, episode_id=3)
        ]
        db.session.add_all(appearances)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    seed_database()