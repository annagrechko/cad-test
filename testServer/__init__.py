from flask import Flask, render_template, g
from flask.ext.login import LoginManager, current_user
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.user = current_user

from testServer import models, views
from models import User


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)



