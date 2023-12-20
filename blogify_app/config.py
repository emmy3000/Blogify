#!/usr/bin/env python3
"""
Environment variables configuration management.
"""
import os


class Config:
    """
    Configuration settings for the Blogify web application.

    - This class defines the configuration parameters used by
      the Blogify Flask application.
    - These parameters include the secret key for session management
      and the database URI.

    Attributes:
        - SECRET_KEY (str): A secret key used for encrypting session data.
        - SQLALCHEMY_DATABASE_URI (str): The URI for the SQLite database
          used by the application.

    Note:
        Ensure that the SECRET_KEY and SQLALCHEMY_DATABASE_URI are set
        in the environment variables to maintain security and avoid
        exposing sensitive information in the source code.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

