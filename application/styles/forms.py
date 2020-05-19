from flask_wtf import FlaskForm
from wtforms import StringField, validators

class StyleForm(FlaskForm):
    name = StringField("Style name", [validators.Length(min=5)])
 
    class Meta:
        csrf = False
