"""
Initialize the Flask application and its extensions.

- This module serves as the entry point for initializing the Flask
  application and configuring its extensions.
- It sets up essential components such as database connectivity, user
  authentication, and email handling.
- Additionally, it imports and registers blueprints for different
  application modules.

Attributes:
    - app: Flask application instance.
    - db: SQLAlchemy database instance.
    - bcrypt: Bcrypt extension for password hashing.
    - login_manager: LoginManager for user session management.
    - mail: Mail extension for email handling.

The module also imports models and registers blueprints
for 'users', 'posts', and 'main'.
"""


from dotenv import load_dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# Load environment variables from .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

# Initialize configuration variables with environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWORD")

# Initialize SQLAlchemy database with the Flask application instance
db = SQLAlchemy(app)

# Initialize Bcrypt for password hashing with the Flask application instance
bcrypt = Bcrypt(app)

# Initialization and managemen of users login sessions with the Flask application instance.
login_manager = LoginManager(app)

# Define the view name for login redirection if user is not authenticated
login_manager.login_view = "users.login"

# Set the message category for login messages
login_manager.login_message_category = "info"

# Initialize Mail extension with the Flask application instance for email handling
mail = Mail(app)

# Import the models module after initializing the app and extensions
from blogify_app.models import User, Post

# Importing the blueprint instances for the 'users', 'posts', and 'main' modules
from blogify_app.users.routes import users
from blogify_app.posts.routes import posts
from blogify_app.main.routes import main

# Registering the blueprints with the Flask application instance
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
