#!/usr/bin/python3

from datetime import datetime
from blogify_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by user ID.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User: The User object associated with the given ID.
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Class representing a user in the blog application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        image_file (str): The filename of the user's profile picture.
        password (str): The hashed password of the user.
        posts (list): List of posts authored by the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """
        String representation of the User object.

        Returns:
            str: A formatted string representing the User object.
        """
        return 'User("{}", "{}", "{}")'.format(self.username, self.email, self.image_file)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Post("{}", "{}")'.format(self.title, self.date_posted)
