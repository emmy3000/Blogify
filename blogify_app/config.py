#!/usr/bin/env python3
"""
Configuration module for the Blogify web application.

This module defines a configuration class, Config, which encapsulates
the configuration parameters needed for the Flask application. These
settings, such as database URI and email server details, are read from
a JSON configuration file for security and flexibility.

The Config class serves as a central location for managing configuration
settings used by the Flask application to customize its behavior and
connect to external services.

Author: [Emeka Emodi] <emodiemeka@gmail.com>
"""

import json

# Load configuration from the JSON file
with open("/etc/config.json") as config_file:
    config = json.load(config_file)


class Config:
    """
    Configuration class for the Blogify web application.

    This class encapsulates the configuration parameters needed
    for the Flask application.

    Attributes:
        SECRET_KEY (str): A secret key used for securely signing
          session cookies and other security-related functions.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy database,
          specifying the database type, username, password, host, port, and
          database name.
        MAIL_SERVER (str): The hostname or IP address of the email server.
        MAIL_PORT (int): The port number to use for connecting to the email
          server.
        MAIL_USE_TLS (bool): A boolean indicating whether to use Transport Layer
          Security (TLS) when connecting to the email server.
        MAIL_USERNAME (str): The username for authenticating with the email server.
        MAIL_PASSWORD (str): The password for authenticating with the email server.

    Note:
        These configuration settings are read from a JSON file for
        security and flexibility. They are used by the Flask application
        to customize its behavior and connect to external services such as
        databases and email servers.
    """

    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("DATABASE_URL")
    MAIL_SERVER = "smtp.office365.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get("EMAIL_USER")
    MAIL_PASSWORD = config.get("EMAIL_PASSWORD")

