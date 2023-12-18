#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create a Flask application instance
app = Flask(__name__)

# Set the secret key for securing session data
app.config['SECRET_KEY'] = '4f4361ae36d8a09864390826f3f8fe4e'

# Set the URI for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Create a Bcrypt instance for password hashing
bcrypt = Bcrypt(app)

# Create a LoginManager instance for handling user login
login_manager = LoginManager(app)

# Set the view to redirect to for login if the user is not logged in
login_manager.login_view = 'login'

# Set the category for displaying login messages
login_manager.login_message_category = 'info'

# Import the models module after initializing the app and extensions
from blogify_app.models import User, Post

# Import the routes module after initializing the app and extensions
from blogify_app import routes
