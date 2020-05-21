from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ComposerForm(FlaskForm):
    name = StringField("Composer name", [validators.required(), validators.length(min=5, max=50)])

    class Meta:
        csrf = False

