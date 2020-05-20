from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ArrangerForm(FlaskForm):
    name = StringField("Arranger name", [validators.required(), validators.length(min=5), validators.length(max=50)])
 
    class Meta:
        csrf = False
