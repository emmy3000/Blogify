#!/usr/bin/env python3
"""
Flask Blueprint for handling custom error pages (404, 403, 500).

- This Blueprint provides error handlers for HTTP status codes
  404 (Not Found), 403 (Forbidden), and 500 (Internal Server Error).
- It renders custom error pages while setting the appropriate
  HTTP status codes for each error scenario.

Usage:
- Include this Blueprint in your Flask app to handle custom error pages.
"""

from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """
    Handle 404 Not Found errors.

    Args:
    - error (Exception): The error object.

    Returns:
    - tuple: A tuple containing the rendered template
      for the 404 error page and the HTTP status code 404.

    - This function is an error handler for 404 Not Found errors.
    - It renders the "errors/404.html" template
      and sets the HTTP status code to 404 before returning the response.
    """
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    Handle 403 Forbidden errors.

    Args:
    - error (Exception): The error object.

    Returns:
    - tuple: A tuple containing the rendered template
      for the 403 error page and the HTTP status code 403.

    - This function is an error handler for 403 Forbidden errors.
    - It renders the "errors/403.html" template
      and sets the HTTP status code to 403 before returning the response.
    """
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error):
    """
    Handle 500 Internal Server Error.

    Parameters:
    - error (Exception): The error object.

    Returns:
    - tuple: A tuple containing the rendered template
     for the 500 error page and the HTTP status code 500.

    - This function is an error handler for 500 Internal Server Error.
    - It renders the "errors/500.html" template and sets the HTTP status code
      to 500 before returning the response.
    """
    return render_template("errors/500.html"), 500
