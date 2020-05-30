from application.concerts.models import Concert

from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, validators
from wtforms.validators import ValidationError

class ConcertForm(FlaskForm):
    name = StringField("Concert name", [validators.required(), validators.length(min=5, max=50)])
    venue = StringField("Concert venue", [validators.required(), validators.length(min=5, max=50)])
    date = StringField("Concert date", [validators.required(), validators.length(min=8, max=10)])
    
    class Meta:
        csrf = False
