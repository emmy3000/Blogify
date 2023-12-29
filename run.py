#!/usr/bin/python3
"""
Run the Flask web application.

- This module initializes and runs the Flask web application
  defined in the 'blogify_app' package.
- It starts the development server
  with debug mode enabled.

Usage: To start the application, execute this script directly
  by executing the command 'python run.py'

Note: Avoid using the development server in a production
  environment.

For configuration and detailed documentation on the application,
refer to the 'blogify_app' package and its modules.
"""

from blogify_app import app

if __name__ == "__main__":
    app.run(debug=True)
