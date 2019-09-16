from flask import Blueprint, request, render_template, flash, redirect
from flask_login import login_required, current_user
from src.forms.restaurant import RestaurantForm, RestaurantEditList
from src.modules.restaurant_helper import save_changes, fetch_restaurants_list_by_user, edit_restaurant_by_id,\
    fetch_restaurant_by_id

# register the restaurant endpoint
restaurant_endpoints = Blueprint('restaurant_endpoints', __name__, template_folder='templates')


@restaurant_endpoints.route('/create_restaurant', methods=['GET', 'POST'])
@login_required
def create_restaurant():
    """
    End point for adding a new Restaurant. It gets the restaurant form and send it over to the save change
    function to persist the changes in the database
    :return: the create restaurant template in case of GET and back to the index in case of successfully created
    restaurant
    """
    form = RestaurantForm(request.form)
    if request.method == 'POST' and form.validate():
        save_changes(form)
        flash('Restaurant created successfully!')
        return redirect('/')

    return render_template('create_restaurant.html', form=form)


@restaurant_endpoints.route('/restaurant_edit_list', methods=['GET', 'POST'])
@login_required
def restaurant_edit_list():
    """
    Endpoint for listing the editable restaurants, fetches the user editable restaurants (the restaurants for
    which the authenticated user is owner) and create a table model to send along with the template to be rendered
    :return: the restaurant edit list template together with the table of editable restaurants
    """
    editable_restaurants = fetch_restaurants_list_by_user(current_user.id)

    if not editable_restaurants:
        flash('No restaurants found, please add a restaurant fist.')
        return redirect('/create_restaurant')
    else:
        # display results
        table = RestaurantEditList(editable_restaurants)
        table.border = True
        return render_template('restaurants_edit_list.html', table=table)


@restaurant_endpoints.route('/edit_restaurant/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_restaurant(id):
    """
    End point for editing an existing Restaurant. It gets the restaurant id to modify and send it over to the edit
    restaurant by id function to persist the changes in the database
    :param id: the id of the restaurant to modify
    :return: the edit restaurant template if it's a GET and back to the restaurant edit list after modifying the
    restaurant if it's a POST
    """
    restaurant = fetch_restaurant_by_id(id)
    form = RestaurantForm(formdata=request.form, obj=restaurant)
    if request.method == 'POST' and form.validate():
        # save edits
        edit_restaurant_by_id(form, id)
        flash('Restaurant updated successfully!')
        return redirect('/restaurant_edit_list')
    return render_template('edit_restaurant.html', form=form)
