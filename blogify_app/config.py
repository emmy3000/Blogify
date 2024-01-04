#!/usr/bin/env python3
"""
Configuration module for the Blogify web application.

This module defines a configuration class, Config,
which encapsulates the configuration parameters needed
for the Flask application. These settings, such as database
URI and email server details, are read from environment
variables for security and flexibility.

The Config class serves as a central location for managing
configuration settings used by the Flask application to customize
its behavior and connect to external services.

Author: [Emeka Emodi] <emodiemeka@gmail.com>
"""

import os


class Config:
    """
    Configuration class for the Blogify web application.

    - This class encapsulates the configuration parameters needed
      for the Flask application.
    - The configuration settings are read from
      environment variables for security and flexibility.

    Attributes:
        SECRET_KEY (str): A secret key used for securely signing
          session cookies and other security-related functions.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy database,
          specifying the database type, username, password, host, port, and
          database name.
        MAIL_SERVER (str): The hostname or IP address of the email
          server.
        MAIL_PORT (int): The port number to use for connecting to the email
          server.
        MAIL_USE_TLS (bool): A boolean indicating whether to use Transport Layer
          Security (TLS) when connecting to the email server.
        MAIL_USERNAME (str): The username for authenticating with the email
          server.
        MAIL_PASSWORD (str): The password for authenticating with the email
          server.

    Note:
        These configuration settings are used by the Flask application to
        customize its behavior and connect to external services such as
        databases and email servers.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
