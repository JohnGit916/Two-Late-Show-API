import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    print("🔄 Resetting database...")
    db.drop_all()
    db.create_all()

    # Create users
    admin = User(username="admin")
    admin.password_hash = "admin123"

    tester = User(username="tester")
    tester.password_hash = "tester123"

    # Create 5 guests
    guests = [
        Guest(name="John Cena", occupation="Wrestler"),
        Guest(name="Beyoncé", occupation="Musician"),
        Guest(name="Elon Musk", occupation="Entrepreneur"),
        Guest(name="Oprah Winfrey", occupation="TV Host"),
        Guest(name="Serena Williams", occupation="Tennis Player"),
    ]

    # Create 5 episodes
    episodes = [
        Episode(date="2025-06-01", number=1),
        Episode(date="2025-06-02", number=2),
        Episode(date="2025-06-03", number=3),
        Episode(date="2025-06-04", number=4),
        Episode(date="2025-06-05", number=5),
    ]

    # Create 5 appearances (1 per episode, rotating guests)
    appearances = [
        Appearance(rating=5, guest=guests[0], episode=episodes[0]),
        Appearance(rating=4, guest=guests[1], episode=episodes[1]),
        Appearance(rating=3, guest=guests[2], episode=episodes[2]),
        Appearance(rating=5, guest=guests[3], episode=episodes[3]),
        Appearance(rating=2, guest=guests[4], episode=episodes[4]),
    ]

    # Add everything to the session
    db.session.add_all([admin, tester])
    db.session.add_all(guests)
    db.session.add_all(episodes)
    db.session.add_all(appearances)
    db.session.commit()

    print("✅ Database seeded successfully with 2 users, 5 guests, 5 episodes, and 5 appearances!")
