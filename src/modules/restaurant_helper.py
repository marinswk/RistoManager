from src.models.restaurant import Restaurant
from app import db
from flask_login import current_user


def fetch_restaurants_list():
    """
    fetches a list of all public restaurants
    :return: the requested list of all public restaurants (sqlalchemy restaurant entity)
    """
    try:
        return Restaurant.query.filter(Restaurant.is_public == True).all()
    except Exception as e:
        raise e


def fetch_restaurants_list_by_user(user_id):
    """
    fetches a list of restaurants belonging to a specific user
    :param user_id: the user for which to fetch the restaurants for
    :return: the requested list of restaurants (sqlalchemy restaurant entity)
    """
    try:
        return Restaurant.query.filter(Restaurant.user_id == user_id).all()
    except Exception as e:
        raise e


def fetch_restaurant_by_id(restaurant_id):
    """
    fetches a single restaurant by its id
    :param restaurant_id: the id of the restaurant to fetch
    :return: the requested sqlalchemy restaurant entity
    """
    try:
        return Restaurant.query.filter(Restaurant.id == restaurant_id).first()
    except Exception as e:
        raise e


def save_changes(form):
    """
    Adds a new restaurant in the database
    :param form: the form containing all the restaurant info
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    restaurant = Restaurant(
        name=form.data['name'],
        address=form.data['address'],
        opening_hours=form.data['opening_hours'],
        style=form.data['style'],
        menu=form.data['menu'],
        is_public=form.data['is_public'],
        user_id=current_user.id
    )

    db.session.add(restaurant)
    db.session.commit()


def edit_restaurant_by_id(form, restaurant_id):
    """
    Save the changes to a restaurant in the database
    :param form: the form containing all the restaurant info
    :param restaurant_id: the id of the restaurant to edit
    """
    Restaurant.query.filter(Restaurant.id == restaurant_id).update(
        dict(
            name=form.data['name'],
            address=form.data['address'],
            opening_hours=form.data['opening_hours'],
            style=form.data['style'],
            menu=form.data['menu'],
            is_public=form.data['is_public']
        )
    )

    db.session.commit()
