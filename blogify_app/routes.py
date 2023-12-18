#!/usr/bin/python3

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from blogify_app import app, db, bcrypt
from blogify_app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from blogify_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    """
    Render the home page with all blog posts.

    Returns:
        str: Rendered HTML template.
    """
    posts = Post.query.all()
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
    return render_template(
        'create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
