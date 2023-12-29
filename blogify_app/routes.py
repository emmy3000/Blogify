#!/usr/bin/python3

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from blogify_app import app, db, bcrypt, mail
from blogify_app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from blogify_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route('/')
@app.route('/home')
def home():
    """
    Render the home page with the latest blog posts.

    - This route retrieves the latest blog posts from the database
      and paginates them for display on the home page.
    - The number of posts per page is set to 5 by default.

    Returns:
        str: Rendered HTML template displaying the latest blog posts.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    """
    Render the about page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register a new user.

    Returns:
        str: Rendered HTML template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You're now able to log", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log in an existing user.

    Returns:
        str: Rendered HTML template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(
                url_for('home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Log in', form=form)


@app.route('/logout')
def logout():
    """
    Log out the current user.

    Returns:
        str: Redirect to the home page.
    """
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    """
    Save and resize the user's profile picture.

    Args:
        form_picture (FileStorage): The user's uploaded
        profile picture.

    Returns:
        str: Filename of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path,
        'static/profile_pics',
        picture_fn)
    form_picture.save(picture_path)
    # Resize picture if >125pixels
    output_size = (125, 125)
    i = Image.open(picture_path)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """
    Render and update the user's account information.

    Returns:
        str: Rendered HTML template.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static',
        filename='profile_pics/' +
                 current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    """
    Create a new blog post.

    Returns:
        str: Rendered HTML template.
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template(
        'create_post.html', title='New Post', form=form, legend='New Post')


@app.route('/post/<int:post_id>')
def post(post_id):
    """
    Render a specific blog post.

    Args:
        post_id (int): The ID of the blog post.

    Returns:
        str: Rendered HTML template.
    """
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    Update an existing blog post.

    Args:
        post_id (int): The ID of the blog post.

    Returns:
        str: Rendered HTML template.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.title.content = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """
    Delete an existing blog post.

    Args:
        post_id (int): The ID of the blog post.

    Returns:
        str: Redirect to the home page.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route('/user/<string:username>')
def user_posts(username):
    """
    Render the page displaying blog posts by a specific user.

    - This route retrieves blog posts authored by the specified user
      and paginates them for display on the user's posts page.
    - The number of posts per page is set to 5 by default.

    Args:
        username (str): The username of the target user.

    Returns:
        str: Rendered HTML template displaying blog posts by the user.

    Raises:
        404: If no user with the specified username is found.
    """
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user). \
        order_by(Post.date_posted.desc()). \
        paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


def send_reset_email(user):
    try:
        token = user.get_reset_token()
        msg = Message('Password Reset Request', sender='emodiemeka@outlook.com', recipients=[user.email])
        msg.body = f'''To reset your password visit the following link:
        {url_for('reset_token', token=token, _external=True)}

        If did not make this request then simply ignore this email and no changes will be made.
        '''
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    """
    Handle user requests to reset their password.

    This route function is responsible for processing user requests
    to reset their password. If the user is already authenticated,
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

    Note:
        - This route is accessible to non-authenticated users only.
        - The `RequestResetForm` class is used for handling the password
          reset request form.
        - Upon successful form submission, a reset email is sent using
          the `send_reset_email` function.
        - A flash message is displayed to inform the user about the
          email being sent.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    """
    Handle user password reset using a token.

    This route function processes user password reset requests using
    a unique token. If the user is already authenticated, they are
    redirected to the home page. The token is verified, and if valid,
    the user is presented with a form to reset their password.

    Methods:
        - GET: Display the password reset form if the token is valid.
        - POST: Process the submitted form, update the user's password,
          and redirect to the login page.

    Args:
        token (str): Unique token associated with the password reset request.

    Returns:
        If the token is invalid or expired, a flash message is displayed,
        and the user is redirected to the password reset request page.
        If the form submission is successful, the user is redirected to
        the login page with a flash message indicating that their password
        has been updated.

    Note:
        - This route is accessible to non-authenticated users only.
        - The `ResetPasswordForm` class is used for handling the password
          reset form.
        - The token is verified using the `verify_reset_token` method
          of the `User` model.
        - Upon successful form submission, the user's password is updated
          in the database.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash("Your password has now been updated! You're now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)