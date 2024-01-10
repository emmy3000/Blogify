#!/usr/bin/env python3

from flask import Blueprint, render_template

landing_bp = Blueprint('landing', __name__)


@landing_bp.route('/')
def landing_page():
    """
    Renders the landing page.

    This function renders the HTML template for the landing page.

    Returns:
        flask.render_template: The rendered HTML template for the landing page.
    """
    return render_template('landing_page.html')

