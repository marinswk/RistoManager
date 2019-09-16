from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# declaration of the flask app plus config, database and login manager
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'user_endpoints.login'

# import of the application various endpoints
# the models imports are needed for generating the migration files for the database
from src.controllers.user import user_endpoints
from src.controllers.restaurants import restaurant_endpoints
from src.models import user
from src.models import restaurant
from src.modules.restaurant_helper import fetch_restaurants_list

# registering the user and restaurant endpoints with the flask app
app.register_blueprint(user_endpoints)
app.register_blueprint(restaurant_endpoints)


@app.route('/')
def index():
    """
    serves the main page of the application (index.html)
    containing a list of available public restaurant both for the anonymous and registered user
    :return: the index.html rendered template
    """
    restaurants = fetch_restaurants_list()
    return render_template('index.html', title='Home', restaurants=restaurants)


if __name__ == '__main__':
    app.run()
