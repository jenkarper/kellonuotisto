from flask import Flask
app = Flask(__name__)

# Tietokanta
from application import views
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sheetmusic.db" # tietokannan nimi (/// = tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa samassa paikassa
app.config["SQLALCHEMY_ECHO"] = True # SQLAlchemy tulostaa kaikki SQL-kyselyt

db = SQLAlchemy(app) # tietokannan käsittelyyn käytettävä db-olio

# Oman sovelluksen toiminnallisuudet
from application import views

from application.pieces import models
from application.pieces import views

from application.composers import models
from application.composers import views

from application.arrangers import models
from application.arrangers import views

from application.styles import models
from application.styles import views

from application.techniques import models
from application.techniques import views

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


# Tietokantataulujen luominen tarvittaessa
db.create_all()

