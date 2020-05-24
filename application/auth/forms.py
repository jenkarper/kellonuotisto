from application.auth.models import User
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, validators
from wtforms.validators import DataRequired, EqualTo, ValidationError
  
class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
  
    class Meta:
        csrf = False # Kytkee 'cross-site request forgery' -hyökkäyksiä vastaan turvautumisen pois päältä

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat password", validators=[DataRequired(), EqualTo("password")])
    #submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")
  
    class Meta:
        csrf = False # Kytkee 'cross-site request forgery' -hyökkäyksiä vastaan turvautumisen pois päältä


