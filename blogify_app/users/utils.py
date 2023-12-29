#!/usr/bin/env python3
"""
Utility functions for user-related operations
in the Flask web application.

- This module provides utility functions used in user-related
  operations, including profile picture handling and password reset
  email sending.
- The functions handle tasks such as saving and resizing user
  profile pictures, generating and sending password reset emails.

For detailed information about each utility function, parameters,
and behavior, refer to the individual function docstrings.

Note: These utilities are used in conjunction with the 'users' Blueprint
routes and forms defined in 'blogify_app/users/routes.py'
and 'blogify_app/users/forms.py'.
"""

import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from blogify_app import app, mail


def save_picture(form_picture):
    """
    Save and resize the user's profile picture.

    This function takes a user's uploaded profile picture,
    generates a unique filename, saves the picture to the
    'static/profile_pics' directory, and resizes it
    to a maximum size of 125x125 pixels.

    Args:
        form_picture (FileStorage): The user's uploaded profile
          picture.

    Returns:
        str: Filename of the saved and resized picture.

    Raises:
        Any exceptions raised during file handling, image processing,
        or saving.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    form_picture.save(picture_path)
    # Resize picture if >125 pixels
    output_size = (125, 125)
    i = Image.open(picture_path)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    """
    Send a password reset email to the user.

    This function generates a unique reset token for the user,
    constructs a password reset email, and sends it to the
    user's email address.

    Args:
        user (User): The user for whom the password reset email
          is to be sent.

    Returns:
        None

    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        token = user.get_reset_token()
        msg = Message(
            "Password Reset Request",
            sender="emodiemeka@outlook.com",
            recipients=[user.email],
        )
        msg.body = f"""To reset your password visit the following link:
        {url_for('reset_token', token=token, _external=True)}

        If you did not make this request, simply ignore this email, and
        no changes will be made to your account.
        """
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
