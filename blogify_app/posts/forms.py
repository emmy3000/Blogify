#!/usr/bin/env python3
"""
Form class for creating a new blog post in the Flask web
application.

- This module defines a form class, 'PostForm,' used for collecting
  and validating information for a new blog post.
- The form includes input fields for the title and content of the
  new blog post, along with a submit button.
- Validators are applied to ensure that both the title and content
  are required.

For detailed information about each form attribute, validators,
and usage, refer to the individual attribute docstrings.

Note: This form is used in the creation of new blog posts
and interacts with the 'Post' model defined in 'blogify_app/models.py'.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


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
