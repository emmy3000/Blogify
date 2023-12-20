"""
Initialize the Flask application and its extensions.
"""

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import the models module after initializing the app and extensions
from blogify_app.models import User, Post

# Import the routes module after initializing the app and extensions
from blogify_app import routes