"""
Initialize the Flask application and its extensions.
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
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

# Initialize SQLAlchemy database with the Flask application instance
db = SQLAlchemy(app)

# Initialize Bcrypt for password hashing with the Flask application instance
bcrypt = Bcrypt(app)

# Initialization and managemen of users login sessions with the Flask application instance.
login_manager = LoginManager(app)

# Define the view name for login redirection if user is not authenticated
login_manager.login_view = 'login'

# Set the message category for login messages
login_manager.login_message_category = 'info'

# Initialize Mail extension with the Flask application instance for email handling
mail = Mail(app)

# Import the models module after initializing the app and extensions
from blogify_app.models import User, Post

# Import the routes module after initializing the app and extensions
from blogify_app import routes