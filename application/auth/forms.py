from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False # Kytkee 'cross-site request forgery' -hyökkäyksiä vastaan turvautumisen pois päältä

