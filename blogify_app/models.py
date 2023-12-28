#!/usr/bin/python3

from dotenv import load_dotenv
from datetime import datetime
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
from blogify_app import db, login_manager, app
from flask_login import UserMixin
import os
import json

load_dotenv()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by user ID.

    - This function is used by Flask-Login to retrieve a User object
      from the database based on the provided user ID.
    - It is part of the user_loader
      callback required by Flask-Login.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User: The User object associated with the given user ID.

    Note:
        - This function is designed to be used with the Flask-Login
          extension.
        - It is invoked automatically by Flask-Login when attempting
          to load a user during a user session.
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Class representing a user in the blog application.

    - This class defines the structure of the User model in the database.
    - Users in the blog application have the following attributes:

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        image_file (str): The filename of the user's profile picture.
        password (str): The hashed password of the user.
        posts (list): List of posts authored by the user.

    Note:
        - The 'id' attribute serves as the primary key in the database.
        - 'username' must be unique and is limited to 20 characters.
        - 'email' must be unique and is limited to 120 characters.
        - 'image_file' is the filename of the user's profile picture and has
            a default value of 'default.jpeg'.
        - 'password' is the hashed password of the user.
        - 'posts' represents the relationship with the 'Post' model,
            allowing access to posts authored by the user.

    Usage:
        - This class is used in conjunction with Flask-SQLAlchemy
          to define the structure of the 'users' table in the database.
        - Instances of this class represent individual users
          with associated attributes.
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
        """
        Verifies the validity of a reset token generated
        by the 'get_reset_token' method.

        Args:
            token (str): The reset token to be verified.

        Returns:
            User: The User object associated with the verified token
                if the token is valid.
            None: If the token is invalid or has expired.

        Raises:
            SignatureExpired: If the token has expired.
            BadSignature: If the token has an invalid signature
              i.e. It has been maliciously tampered with by a hacker.
        """
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
         Returns a string representation of the User object.

        - This method is called by the built-in repr() function
         and is used to create a string representation of the User object
         in a format that provides a concise and human-readable summary.

        Returns:
            str: A formatted string representing the User object.
              The format includes the username, email, and image_file
              attributes of the User.
        """
        return 'User("{}", "{}", "{}")'.format(self.username, self.email, self.image_file)


class Post(db.Model):
    """
    Class representing a blog post in the application.

    - This class defines the structure of the Post model in the database.
    - Blog posts in the application have the following attributes:

    Attributes:
        id (int): The unique identifier for the post.
        title (str): The title of the post.
        date_posted (datetime): The date and time when the post was created.
        content (str): The content of the post.
        user_id (int): The ID of the user who authored the post.

    Note:
        - The 'id' attribute serves as the primary key in the database.
        - 'title' represents the title of the blog post and is limited to
          120 characters.
        - 'date_posted' is the date and time when the post was created,
          with a default value set to the current UTC time.
        - 'content' contains the textual content of the blog post.
        - 'user_id' is a foreign key referencing the 'id' column
          of the 'users' table, indicating the user who authored
          the post.

    Usage:
        - This class is used in conjunction with Flask-SQLAlchemy
          to define the structure of the 'posts' table in the database.
        - Instances of this class represent individual blog posts
          with associated attributes.

    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Post object.

        - This method is called by the built-in repr() function
          and is used to create a string representation of the
          Post object in a format that provides a concise
          and human-readable summary.

        Returns:
            str: A formatted string representing the Post object.
            The format includes the title and 'date_posted' attributes
            of the Post.
        """
        return 'Post("{}", "{}")'.format(self.title, self.date_posted)
