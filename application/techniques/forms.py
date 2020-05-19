from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TechniqueForm(FlaskForm):
    name = StringField("Technique name", [validators.Length(min=3), validators.Length(max=20)])
 
    class Meta:
        csrf = False
