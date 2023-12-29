#!/usr/bin/env python3
"""
Defines FlaskForm classes for user registration, login,
account updates, post creation, and password reset.

This module contains form classes that define the structure
of web forms used in the Blogify web application. These forms
are responsible for collecting and validating user input
related to user registration, login, account updates, post
creation, and password reset.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogify_app.models import User


class RegistrationForm(FlaskForm):
    """
    Form class for user registration.

    This class defines a form used for collecting and validating
    user registration information.

    Attributes:
        username (StringField): Input field for the chosen username.
            - Validators: DataRequired (ensures a value is provided),
              Length (ensures the length is between 2 and 20 characters).
        email (StringField): Input field for the user's email address.
            - Validators: DataRequired (ensures a value is provided),
              Email (validates that the input is a valid email address).
        password (PasswordField): Input field for the chosen password.
            - Validators: DataRequired (ensures a value is provided).
        confirm_password (PasswordField): Input field to confirm the chosen
          password.
            - Validators: DataRequired (ensures a value is provided),
              EqualTo('password') (validates that it matches the chosen
              password).
        submit (SubmitField): Button to submit the registration form.

    Validators:
        - `username`: Enforces that the username is required
          and within a length range of 2 to 20 characters.
        - `email`: Enforces that a valid email address is provided.
        - `password`: Enforces that a password is required.
        - `confirm_password`: Enforces that the confirmation password
          is required and matches the chosen password.
    """

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """
        Validate the uniqueness of the chosen username.

        Args:
            username (StringField): User's chosen username.

        Raises:
            ValidationError: If the username is already taken.
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("That username is taken, Please choose another one")

    def validate_email(self, email):
        """
        Validate the uniqueness of the chosen email address.

        Args:
            email (StringField): User's email address.

        Raises:
            ValidationError: If the email address is already taken.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("That email is taken, Please choose another one")


class LoginForm(FlaskForm):
    """
    Form class for user login.

    This class defines a form used for collecting and validating
    user login information.

    Attributes:
        email (StringField): Input field for the user's email address.
            - Validators: DataRequired (ensures a value is provided),
              Email (validates that the input is a valid email address).
        password (PasswordField): Input field for the user's password.
            - Validators: DataRequired (ensures a value is provided).
        remember (BooleanField): Checkbox for remembering the user.
        submit (SubmitField): Button to submit the login form.

    Validators:
        - `email`: Enforces that a valid email address is provided.
        - `password`: Enforces that a password is required.
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    """
    Form class for updating user account information.

    This class defines a form used for collecting and validating
    updated user account information.

    Attributes:
        username (StringField): Input field for the updated username.
            - Validators: DataRequired (ensures a value is provided),
              Length (ensures the length is between 2 and 20 characters).
        email (StringField): Input field for the updated email address.
            - Validators: DataRequired (ensures a value is provided),
              Email (validates that the input is a valid email address).
        picture (FileField): Input field for updating the profile picture file.
            - Validators: FileAllowed (limits allowed file extensions
              to 'jpg' and 'png').
        submit (SubmitField): Button to submit the update account form.

    Validators:
        - `username`: Enforces that the updated username is required
          and within a length range of 2 to 20 characters.
        - `email`: Enforces that a valid email address is provided.
        - `picture`: Enforces that the uploaded file has an allowed
          extension ('jpg' or 'png').
    """

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_username(self, username):
        """
        Validate the uniqueness of the updated username.

        Args:
            username (StringField): Updated username.

        Raises:
            ValidationError: If the updated username is already taken.
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None and username.data != current_user.username:
            raise ValidationError("That username is taken, Please choose another one")

    def validate_email(self, email):
        """
        Validate the uniqueness of the updated email address.

        Args:
            email (StringField): Updated email address.

        Raises:
            ValidationError: If the updated email address is already taken.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None and email.data != current_user.email:
            raise ValidationError("That email is taken, Please choose another one")


class PostForm(FlaskForm):
    """
    Form class for creating a new blog post.

    This class defines a form used for collecting and validating
    information for a new blog post.

    Attributes:
        title (StringField): Input field for the title of the
          new blog post.
            - Validators: DataRequired (ensures a value is provided).
        content (TextAreaField): Input field for the content
          of the new blog post.
            - Validators: DataRequired (ensures a value is provided).
        submit (SubmitField): Button to submit the new blog post form.

    Validators:
        - `title`: Enforces that the title for the new blog post is required.
        - `content`: Enforces that the content for the new blog
          post is required.
    """

    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")


class RequestResetForm(FlaskForm):
    """
    Form class for handling user requests to reset their password.

    Attributes:
        email (StringField): Input field for the user's email address.
            Validators: DataRequired, Email
        submit (SubmitField): Button to submit the password reset request.

    Note:
        - This form is used to collect the user's email address when
          initiating the password reset process.
        - The email field must
         be filled with a valid email address for the process to proceed.
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        """
        Validate the email address entered for password reset.

        Args:
            email (StringField): The email address entered
              by the user.

        Raises:
            ValidationError: If no user account is found
              with the entered email.
              - The user must register first to initiate
                a password reset.

        Note:
            - This method checks if a user account exists
              with the provided email.
            - If no account is found, a ValidationError is raised,
              indicating that the user must register first before
              initiating a password reset.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class ResetPasswordForm(FlaskForm):
    """
    Form for resetting a user's password.

    Attributes:
        password (PasswordField): Input field for the new password.

    Validators:
        - `password`: Enforces that a new password
          is required (DataRequired).

        confirm_password (PasswordField): Input field to confirm
          the new password.
        - Validators:
            - `DataRequired`: Ensures a value is provided.
            - `EqualTo('password')`: Validates that it matches
              the 'password' input.

        submit (SubmitField): Button to submit the password
          reset request.
    """

    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")
