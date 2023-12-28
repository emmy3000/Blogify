#!/usr/bin/env python3

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogify_app.models import User


class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    Attributes:
        username (StringField): User's chosen username.
        email (StringField): User's email address.
        password (PasswordField): User's chosen password.
        confirm_password (PasswordField): Confirm the user's chosen password.
        submit (SubmitField): Button to submit the registration form.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

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
            raise ValidationError('That username is taken, Please choose another one')

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
            raise ValidationError('That email is taken, Please choose another one')


class LoginForm(FlaskForm):
    """
    Form for user login.

    Attributes:
        email (StringField): User's email address.
        password (PasswordField): User's password.
        remember (BooleanField): Checkbox for remembering the user.
        submit (SubmitField): Button to submit the login form.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """
    Form for updating user account information.

    Attributes:
        username (StringField): Updated username.
        email (StringField): Updated email address.
        picture (FileField): Updated profile picture file.
        submit (SubmitField): Button to submit the update account form.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Piture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

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
            raise ValidationError('That username is taken, Please choose another one')

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
            raise ValidationError('That email is taken, Please choose another one')


class PostForm(FlaskForm):
    """
    Form for creating a new blog post.

    Attributes:
        title (StringField): Title of the new blog post.
        content (TextAreaField): Content of the new blog post.
        submit (SubmitField): Button to submit the new blog post form.
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


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
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """
        Validate the email address entered for password reset.

        Args:
            email (StringField): The email address entered by the user.

        Raises:
            ValidationError: If no user account is found with the entered email.
                The user must register first to initiate a password reset.

        Note:
            - This method checks if a user account exists
              with the provided email.
            - If no account is found, a ValidationError is raised,
              indicating that the user must register first before initiating
              a password reset.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
