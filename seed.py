#!/usr/bin/env python3
# server/seed.py

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():

    # Delete all rows in the "earthquakes" table
    User.query.delete()

    # Add several Earthquake instances to the "earthquakes" table
    db.session.add(User(username="user1", email="user1@example.com"))
    db.session.add(User(username="user2", email="user2@example.com"))

    # Commit the transaction
    db.session.commit()

    Fixed Expenses