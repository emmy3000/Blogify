#!/usr/bin/env python3
"""
Blog post-related routes for the Flask web application.

- This module defines routes for handling blog post-related
  operations, including creating, viewing, updating, and deleting
  blog posts.
- The routes are associated with the 'posts' Blueprint.

For detailed information about each route, parameters, and behavior,
refer to the individual route docstrings.

Note: These routes interact with the 'Post' model and the 'PostForm'
form defined in 'blogify_app/models.py' and 'blogify_app/posts/forms.py'
respectively.
"""


from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from blogify_app import db
from blogify_app.models import Post
from blogify_app.posts.forms import PostForm

posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    """
    Create a new blog post.

    This route handles both GET and POST requests
    to create a new blog post.

    Methods:
        - GET: Displays the form to create a new blog post.
        - POST: Processes the submitted form, creates a new blog
          post in the database, and redirects to the home page
          upon success.

    Returns:
        str: Rendered HTML content based on the request.

    Raises:
        Any exceptions raised during form validation, database
        operations, or template rendering.
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("home"))
    return render_template(
        "create_post.html", title="New Post", form=form, legend="New Post"
    )


@posts.route("/post/<int:post_id>")
def post(post_id):
    """
    Render a specific blog post.

    This route renders a specific blog post based
    on the provided post ID.

    Args:
        post_id (int): The ID of the blog post to be rendered.

    Returns:
        str: Rendered HTML content for the specified blog post.

    Raises:
        404 Not Found: If the specified post ID does not exist
          in the database.
    """
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    """
    Update an existing blog post.

    This route handles both GET and POST requests to update
    an existing blog post based on the provided post ID.

    Args:
        post_id (int): The ID of the blog post to be updated.

    Returns:
        str: Rendered HTML content based on the request.

    Raises:
        403 Forbidden: If the current user is not the author
          of the specified blog post.
        404 Not Found: If the specified post ID does not exist
          in the database.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        "create_post.html", title="Update Post", form=form, legend="Update Post"
    )


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    """
    Delete an existing blog post.

    This route handles a POST request to delete an existing
    blog post based on the provided post ID.

    Args:
        post_id (int): The ID of the blog post to be deleted.

    Returns:
        str: Redirect to the home page.

    Raises:
        403 Forbidden: If the current user is not the author
          of the specified blog post.
        404 Not Found: If the specified post ID does not exist
          in the database.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("home"))
