from application.auth.models import User
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, validators
from wtforms.validators import DataRequired, EqualTo, ValidationError
  
class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), validators.length(min=5, max=30)])
    username = StringField("Username", validators=[DataRequired(), validators.length(min=5, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), validators.length(min=5, max=15)])
  
    class Meta:
        csrf = False # Kytkee 'cross-site request forgery' -hyökkäyksiä vastaan turvautumisen pois päältä

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), validators.length(min=5, max=30)])
    username = StringField("Username", validators=[DataRequired(), validators.length(min=5, max=15)])
    admin = BooleanField("Admin")
    password = PasswordField("Password", validators=[DataRequired(), validators.length(min=5, max=15)])
    password2 = PasswordField("Repeat password", validators=[DataRequired(), EqualTo("password")])
    #submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")
  
    class Meta:
        csrf = False # Kytkee 'cross-site request forgery' -hyökkäyksiä vastaan turvautumisen pois päältä


