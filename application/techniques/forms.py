from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TechniqueForm(FlaskForm):
    name = StringField("Technique name", [validators.required(), validators.length(min=3), validators.length(max=20)])
 
    class Meta:
        csrf = False
