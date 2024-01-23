"""
Initialize the Flask application and its extensions.

- This module serves as the entry point for initializing
  the Flask application and configuring its extensions.
- It sets up essential components such as database connectivity,
  user authentication, and email handling.
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

 Author: Emeka Emodi<emodiemeka@gmail.com>
"""

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blogify_app.config_production import Config

# Load environment variables from .env file
load_dotenv()

# Initialize SQLAlchemy database with Flask app
db = SQLAlchemy()

# Initialize Bcrypt for password hashing with Flask app
bcrypt = Bcrypt()

# Init. and handle user login sessions with Flask app
login_manager = LoginManager()

# Define view name for login redirection if user not authenticated
login_manager.login_view = "users.login"

# Set message category for login messages
login_manager.login_message_category = "info"

# Initialize Mail extension with Flask app for email handling
mail = Mail()

# Import models module after initializing app and extensions
from blogify_app.models import User, Post


def create_app(config_class=Config):
    """
    Factory function to create the Blogify Flask application.

    This function initializes and configures the Flask application,
    along with associated extensions such as Flask-SQLAlchemy, Flask-Bcrypt,
    Flask-Login, and Flask-Mail. It registers blueprints for different
    application components (users, posts, main, landing_bp, and errors)
    to organize routes and views.

    Args:
        config_class (class, optional): The configuration class to use.
            Defaults to Config.

    Returns:
        Flask: The configured Flask application instance.

    Usage:
        - app = create_app()
        - app.run()

    Notes:
        - The configuration parameters are set using the provided
          config_class or the default Config class.
        - The database, password hashing, login management, and email
          handling are initialized and associated with the app.
        - Blueprints are registered to organize routes for different
          components of the application (users, posts, main, landing_bp, and errors).
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from blogify_app.users.routes import users
    from blogify_app.posts.routes import posts
    from blogify_app.main.routes import main
    from blogify_app.landing_bp.routes import landing_bp
    from blogify_app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(landing_bp)
    app.register_blueprint(errors)

    return app
