from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ComposerForm(FlaskForm):
    name = StringField("Composer name", [validators.Length(min=5)])

    class Meta:
        csrf = False

