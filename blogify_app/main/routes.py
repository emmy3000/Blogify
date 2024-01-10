#!/usr/bin/env python3
"""
Routes for the main section of the Flask web application.

- This module defines routes for the main section of the web
  application, including rendering the home page with the latest
  blog posts and an about page.
- The 'home' route retrieves the latest blog posts from the database,
  paginates them, and renders the 'home.html' template.
- The 'about' route renders the 'about.html' template to provide
  information about the application or organization.

For detailed information about each route and its functionality,
refer to the individual route docstrings.

Note: The routes interact with the 'Post' model defined
in 'blogify_app/models.py' to retrieve and display blog posts.
"""

from flask import render_template, request, Blueprint
from blogify_app.models import Post

main = Blueprint("main", __name__)


@main.route("/home")
def home():
    """
    Render the home page with the latest blog posts.

    - This route retrieves the latest blog posts from the database
      and paginates them for display on the home page.
    - The number of posts per page is set to 5 by default.

    Returns:
        str: Rendered HTML template displaying the latest blog posts.
    """
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    """
    Render the about page.

    This route renders the 'about.html' template to provide
    information about the application or organization.

    Returns:
        str: Rendered HTML content for the about page.

    Raises:
        Any exceptions raised by the `render_template` function.
    """
    return render_template("about.html", title="About")
