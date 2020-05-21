from flask_wtf import FlaskForm
from wtforms import StringField, validators

class StyleForm(FlaskForm):
    name = StringField("Style name", [validators.required(), validators.length(min=5, max=20)])
 
    class Meta:
        csrf = False
