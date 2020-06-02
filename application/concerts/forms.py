from application.concerts.models import Concert

from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, validators
from wtforms.validators import ValidationError

class ConcertForm(FlaskForm):
    name = StringField("Concert name", [validators.required(), validators.length(min=5, max=50)])
    venue = StringField("Concert venue", [validators.required(), validators.length(min=5, max=50)])
    date = StringField("Concert date", [validators.required(), validators.length(min=8, max=10)])

    def validate_name(self, name):
        concert = Concert.query.filter_by(name=name.data).first()
        if concert is not None:
            raise ValidationError("Tämän niminen konsertti on jo tietokannassa. Ole hyvä ja tarkenna (esimerkiksi lisäämällä vuosiluku).")
    
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    newname = StringField("Concert name", [validators.required(), validators.length(min=5, max=50)])
    newvenue = StringField("Concert venue", [validators.required(), validators.length(min=5, max=50)])
    newdate = StringField("Concert date", [validators.required(), validators.length(min=8, max=10)])

    def validate_name(self, name):
        concert = Concert.query.filter_by(name=name.data).first()
        if concert is not None:
            raise ValidationError("Tämän niminen konsertti on jo tietokannassa. Ole hyvä ja tarkenna (esimerkiksi lisäämällä vuosiluku).")
    
    class Meta:
        csrf = False
