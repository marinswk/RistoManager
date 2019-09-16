from app import db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from src.models.user import User
from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm

# register the user endpoints that allow password authenticated login to the web application
user_endpoints = Blueprint('user_endpoints', __name__, template_folder='templates')


@user_endpoints.route('/login', methods=['GET', 'POST'])
def login():
    """
    Endpoint for serving the login page template and logging in a user. It checks if the user is already
    authenticated, if not gets the login form and performs password and username checks in order to authenticate the
    user.
    Also handle the next page request in case the user was redirected to the login page from other parts of the
    application
    :return: the requested authenticated forms
    """
    # checks if the user is already authenticated and redirect it back to the index page in case
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # validates the user login form
    form = LoginForm()
    if form.validate_on_submit():
        # fetch the user from the database
        user = User.query.filter_by(username=form.username.data).first()

        # validates user and user password (flashes error and redirect to login page in case of wrong user or
        # password)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user_endpoints.login'))

        # the user is authenticated, perform the login (with flask login module)
        login_user(user, remember=form.remember_me.data)
        # fill the next page if the next arg is set in the request
        next_page = request.args.get('next')

        # if the next arg is not set, redirect to the index page
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        # redirect to the next page in case of set next arg
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@user_endpoints.route('/logout')
def logout():
    """
    Endpoint for logging a user out via the flask_login module.
    :return: redirect to index page
    """
    logout_user()
    return redirect(url_for('index'))


@user_endpoints.route('/register', methods=['GET', 'POST'])
def register():
    """
    Endpoint for registering a new user. Returns the register form in case of GET or handle the user registration
    in case of POST.
    :return: the requested register form for GET or the login template in case of successful POST
    """
    # checks if the current user is already authenticated, if yes redirect to the index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # validates the user registration form
    form = RegistrationForm()
    if form.validate_on_submit():
        # if the form is valid, register a new user and save him in the database
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user_endpoints.login'))
    return render_template('register.html', title='Register', form=form)