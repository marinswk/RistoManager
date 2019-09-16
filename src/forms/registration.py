from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from src.models.user import User


class RegistrationForm(FlaskForm):
    """
    Flask form to handle the login data needed for registering a user
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        manages the username validation of the form. Checks if the user is already existing in the db
        and returns an error in case
        :param username: the username to validate
        :return: raise an exception in case in which the user already exist
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """
        manages the email validation of the form. Checks if the email is already existing in the db
        and returns an error in case
        :param email: the email to validate
        :return: raise an exception in case in which the email already exist
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')