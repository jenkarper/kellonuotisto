from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class ArrangerForm(FlaskForm):
    name = StringField("Arranger name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False


class ComposerForm(FlaskForm):
    name = StringField("Composer name", [validators.required(), validators.length(min=3, max=50)])

    class Meta:
        csrf = False


class StyleForm(FlaskForm):
    name = StringField("Style name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False


class TechniqueForm(FlaskForm):
    name = StringField("Technique name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    newname = StringField("New name", [validators.required(), validators.length(min=3, max=50)])

    class Meta:
        csrf = False

class DeleteForm(FlaskForm):
    delete = BooleanField("Delete row")

    class Meta:
        csrf = False



