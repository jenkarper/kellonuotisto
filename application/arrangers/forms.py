from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ArrangerForm(FlaskForm):
    name = StringField("Arranger name", [validators.Length(min=5)])
 
    class Meta:
        csrf = False
