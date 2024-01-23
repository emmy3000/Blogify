#!/usr/bin/env python3
"""
Configuration module for the Blogify web application in production.

This module defines a configuration class, Config, which encapsulates
the parameters required for the Flask application in a production environment.
Settings such as the database URI and email server details are securely stored
and read from a JSON configuration file.

The Config class serves as a centralized location for managing configuration
settings used by the Flask application. It provides essential information
for customizing the behavior of the application and establishing connections
with external services.

Author: [Emeka Emodi] <emodiemeka@gmail.com>
"""

import json

# Load configuration from the JSON file containing environment variables.
with open("/etc/config.json") as config_file:
    config = json.load(config_file)


class Config:
    """
    Configuration class for the Blogify web application in production.

    This class encapsulates essential configuration parameters for the Flask
    application during the production phase.

    Attributes:
        SECRET_KEY (str): A secret key used for securely signing
          session cookies and other security-related functions.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy
          database, specifying the database type, username, password,
          host, port, and database name.
        MAIL_SERVER (str): The hostname or IP address of the email server.
        MAIL_PORT (int): The port number to use for connecting
          to the email server.
        MAIL_USE_TLS (bool): A boolean indicating whether to use
          Transport Layer Security (TLS) when connecting to the email server.
        MAIL_USERNAME (str): The username for authenticating the email server.
        MAIL_PASSWORD (str): The password for authenticating the email server.

    Note:
        These configuration settings are securely read from a JSON file
        for improved security and flexibility. They play a crucial role
        in customizing the behavior of the Flask application and establishing
        connections with external services, such as databases and email
        servers, during the production phase.
    """

    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("DATABASE_URL")
    MAIL_SERVER = config.get("MAIL_SERVER_KEY")
    MAIL_PORT = int(config.get("MAIL_PORT_KEY"))
    MAIL_USE_TLS = config.get("MAIL_USE_TLS_KEY").lower() == "true"
    MAIL_USERNAME = config.get("EMAIL_USER")
    MAIL_PASSWORD = config.get("EMAIL_PASSWORD")
