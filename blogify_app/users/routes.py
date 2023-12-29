#!/usr/bin/env python3
"""
User-related routes for the Flask web application.

- This module defines routes responsible for user-related operations,
  including user registration, login, logout, account management,
  and password reset functionality.
- It utilizes the Flask Blueprint 'users' for organization and
  modularity.
- The routes support both GET and POST requests for various operations.

For detailed information about each route's behavior, refer to the
individual route function docstrings.

Note: The 'users' Blueprint is registered in the 'blogify_app/__init__.py'
file to be incorporated into the main application.
"""

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blogify_app import db, bcrypt
from blogify_app.models import User, Post
from blogify_app.users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateAccountForm,
    RequestResetForm,
    ResetPasswordForm,
)
from blogify_app.users.utils import save_picture, send_reset_email

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user.

    - This route handles the registration process for new users.
    - It supports both GET and POST requests.

    Methods:
        - GET: Displays the registration form.
        - POST: Processes the submitted form, creates a new user
          in the database, and redirects to the login page upon
          successful registration.

    Returns:
        str: Rendered HTML content based on the request.

    Raises:
        Any exceptions raised during form validation,
        password hashing, database operations, or template rendering.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You're now able to log in.", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in an existing user.

    - This route handles user authentication, allowing existing users
      to log in.
    - It supports both GET and POST requests.

    Methods:
        - GET: Displays the login form.
        - POST: Processes the submitted form, checks user credentials,
          and logs in the user if valid.

    Returns:
        str: Rendered HTML content based on the request.

    Raises:
        Any exceptions raised during form validation, database queries,
        password verification, or template rendering.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful, Please check email and password", "danger")
    return render_template("login.html", title="Log in", form=form)


@users.route("/logout")
def logout():
    """
    Log out the current user.

    This route logs out the currently authenticated user,
    ending their session.

    Returns:
        str: Redirect to the home page.

    Raises:
        Any exceptions raised during the logout process.
    """
    logout_user()
    return redirect(url_for("main.home"))


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """
    Render and update the user's account information.

    This route handles both GET and POST requests to display
    and update the user's account information.

    Methods:
        - GET: Displays the account information form with the current
          user's data pre-filled.
        - POST: Processes the submitted form, updates the user's account
          information, and redirects to the account page upon success.

    Returns:
        str: Rendered HTML content based on the request.

    Raises:
        Any exceptions raised during form validation, picture saving,
        database updates, or template rendering.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated", "success")
        return redirect(url_for("users.account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )


@users.route("/user/<string:username>")
def user_posts(username):
    """
    Render the page displaying blog posts by a specific user.

    - This route retrieves blog posts authored by the specified user
      and paginates them for display on the user's posts page.
    - The number of posts per page is set to 5 by default.

    Args:
        username (str): The username of the target user.

    Returns:
        str: Rendered HTML template displaying blog posts
        by the user.

    Raises:
        404: If no user with the specified username is found.
    """
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("user_posts.html", posts=posts, user=user)


@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    """
    Handle user requests to reset their password.

    - This route function is responsible for processing user requests
      to reset their password.
    - If the user is already authenticated,
      they are redirected to the home page. Otherwise, a form is
      displayed to collect the user's email address for initiating
      the password reset process.

    Methods:
        - GET: Display the password reset request form.
        - POST: Process the submitted form, send a password reset
          email, and redirect to the login page.

    Returns:
        If the form submission is successful, the user is redirected
        to the login page with a flash message indicating that an email
        with reset instructions has been sent. Otherwise, the reset
        request form is displayed.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(
            "An email has been sent with instructions to reset your password.", "info"
        )
        return redirect(url_for("users.login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    """
    Handle user password reset using a token.

    - This route function processes user password reset requests
      using a unique token.
    - If the user is already authenticated, they are
      redirected to the home page. The token is verified,
      and if valid, the user is presented with a form to reset
      their password.

    Methods:
        - GET: Display the password reset form if the token is valid.
        - POST: Process the submitted form, update the user's password,
          and redirect to the login page.

    Args:
        token (str): Unique token associated with the password
        reset request.

    Returns:
        - If the token is invalid or expired, a flash message is displayed,
          and the user is redirected to the password reset request page.
        - If the form submission is successful, the user is redirected to
          the login page with a flash message indicating that their password
          has been updated.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token.", "warning")
        return redirect(url_for("users.reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash(
            "Your password has now been updated! You're now able to log in", "success"
        )
        return redirect(url_for("users.login"))
    return render_template("reset_token.html", title="Reset Password", form=form)
