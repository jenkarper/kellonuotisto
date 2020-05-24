from flask import Flask
app = Flask(__name__)

# Tietokanta
from application import views
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sheetmusic.db"
app.config["SQLALCHEMY_ECHO"] = True # SQLAlchemy tulostaa kaikki SQL-kyselyt

db = SQLAlchemy(app)

# Oman sovelluksen toiminnallisuudet
from application import views

from application.pieces import models
from application.pieces import views

from application.supplements import models
from application.supplements import views

from application.auth import models
from application.auth import views

# Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Viiteavainten tarkistus
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Tietokantataulujen luominen tarvittaessa
db.create_all()

