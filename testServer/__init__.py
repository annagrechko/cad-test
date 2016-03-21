from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
login_manager = LoginManager()


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from testServer import models, views


