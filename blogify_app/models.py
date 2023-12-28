#!/usr/bin/python3

from dotenv import load_dotenv
from datetime import datetime
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
from blogify_app import db, login_manager, app
from flask_login import UserMixin
import os
import json

# Load environment variables from .env file
load_dotenv()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


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

    def get_reset_token(self):
        """
        Generate a time-sensitive reset token for the user.

        - This method creates a reset token for the user by signing a
        JSON object containing the user's ID using a timestamped
        signature.
        - The token is used for securely resetting the user's
        password.

        Returns:
            str: A signed token containing the user's ID.
        """
        s = TimestampSigner(app.config['SECRET_KEY'])
        signed_value = s.sign(json.dumps({'user_id': self.id}))
        return signed_value

    @staticmethod
    def verify_reset_token(token):
        s = TimestampSigner(app.config['SECRET_KEY'])
        try:
            unsigned_value = s.unsign(token, max_age=1800, return_timestamp=True)
            user_id = json.loads(unsigned_value[0].decode('utf-8'))['user_id']
        except SignatureExpired:
            print('Token has expired.')
            return None
        except BadSignature:
            print('Invalid signature.')
            return None
        return User.query.get(user_id)

    def __repr__(self):
        """
        String representation of the User object.

        Returns:
            str: A formatted string representing the User object.
        """
        return 'User("{}", "{}", "{}")'.format(self.username, self.email, self.image_file)


class Post(db.Model):
    """
    Class representing a blog post in the application.

    Attributes:
        id (int): The unique identifier for the post.
        title (str): The title of the post.
        date_posted (datetime): The date and time when the post was created.
        content (str): The content of the post.
        user_id (int): The ID of the user who authored the post.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        String representation of the Post object.

        Returns:
            str: A formatted string representing the Post object.
        """
        return 'Post("{}", "{}")'.format(self.title, self.date_posted)
