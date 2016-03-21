from testServer import db, login_manager
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True
        #Returns True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)

    def is_active(self):
        return True
        #Returns True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).


    def is_anonymous(self):
        return False
        #Returns True if this is an anonymous user. (Actual users should return False instead.)

    def get_auth_token(self):
        #Returns an authentication token (as unicode) for the user. The auth token should uniquely identify the user, and preferably not be guessable by public information about the user such as their UID and name - nor should it expose such information.
        return login_manager.make_secure_token()

    def get_id(self):
        return unicode(self.id)
