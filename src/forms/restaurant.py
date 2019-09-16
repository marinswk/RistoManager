from wtforms import Form, StringField, BooleanField
from flask_table import Table, Col, LinkCol, BoolCol


class RestaurantForm(Form):
    """
    Flask form to handle the registration and edit of a restaurant
    """
    name = StringField('Name')
    address = StringField('Address')
    opening_hours = StringField('Opening Hours')
    style = StringField('Style')
    menu = StringField('Menu')
    is_public = BooleanField('Is Public')


class RestaurantEditList(Table):
    """
    Flask table to handle the listing of the authenticated user owned restaurants
    """
    id = Col('Id', show=False)
    name = Col('Name')
    address = Col('Address')
    opening_hours = Col('Opening Hours')
    style = Col('Style')
    menu = Col('Menu')
    is_public = BoolCol('Is Public')
    edit = LinkCol('Edit', 'restaurant_endpoints.edit_restaurant', url_kwargs=dict(id='id'))
