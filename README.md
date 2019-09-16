# RistoManager
 Basic Password authenticated Flask Application

**Installation**

To run the application you need to create a python virtual environment, after activating it, simply install all the packages in the requirements.txt file.
for example via
	pip install -r requirements.txt

After the requirements are installed and the virtual environment is activated you can just use the command:
	flask run
this will just run a local server with the application at localhost:5000

The database comes already with a registered Admin user:
username: admin
password: admin

**Application**

The application is divided into various folders, to better manage the files and code:


RistoManager
	migrations
	src
		controllers
		forms
		models
		modules
	static
	templates

The **migrations** folder contains all the necessary informations for alembic to work. Alembic is the database migration package that is recognising the changes in the flask sqlalchemy models and updating the db.
commands example:
	flask db migrate
	flask db upgrade

The **src** folder contains the source code of the webserver.

the **controllers** folder contains the various endpoints that the application is exposing, divided into python files grouping the methods and functions based on their usage:
the user.py file contains all the endpoints regarding the user managent (login, logout, register)
	the restaurant.py file contains all the endpoints regarding the restaurant managent (create new, edit, list…)

the **forms** folder contains a collection of flask forms and flask tables used to better manage the showing of those entities in the UI and for better manage the edit and creation. The forms are also divided into user (login.py and registration.py) and restaurant forms.

the **models** folder contains 1to1 representation of the database tables for user and restaurant. The python package used for managing the database connection is SqlAlchemy.

the **static** folded (empty) could contain future CSS/Javascript/images to be served publicly in the website along with the HTML templates.

the **templates** folder is holding all the Jinja2 templates that are served by the various endpoints.

    base.html serves as common ground and style for all the other templates.
	_formhelpers.html is a utility to manage the showing and the management of the flask_forms
	the rest of the templates are divided into restaurant (edit, list, create) and user (login, register) 

**Further readings**
For delving and better understanding the code, every method is commented with an explanation of its usage and eventual parameters, plus an explanation of the most complicated passages, line by line.
