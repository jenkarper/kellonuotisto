from application.supplements.models import Arranger, Composer, Style, Technique

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators
from wtforms.validators import ValidationError


class ArrangerForm(FlaskForm):
    name = StringField("Arranger name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        arranger = Arranger.query.filter_by(name=name.data).first()
        if arranger is not None:
            raise ValidationError("This arranger already exists in the database.")


class ComposerForm(FlaskForm):
    name = StringField("Composer name", [validators.required(), validators.length(min=3, max=50)])

    class Meta:
        csrf = False

    def validate_name(self, name):
        composer = Composer.query.filter_by(name=name.data).first()
        if composer is not None:
            raise ValidationError("This composer already exists in the database.")


class StyleForm(FlaskForm):
    name = StringField("Style name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        style = Style.query.filter_by(name=name.data).first()
        if style is not None:
            raise ValidationError("This style already exists in the database.")


class TechniqueForm(FlaskForm):
    name = StringField("Technique name", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        technique = Technique.query.filter_by(name=name.data).first()
        if technique is not None:
            raise ValidationError("This technique already exists in the database.")

class EditForm(FlaskForm):
    newname = StringField("New name", [validators.required(), validators.length(min=3, max=50)])

    class Meta:
        csrf = False

class DeleteForm(FlaskForm):
    delete = BooleanField("Delete row")

    class Meta:
        csrf = False





