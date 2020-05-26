from application.pieces.models import Piece

from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, validators
from wtforms.validators import ValidationError

# uuden rivin luonti
class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    composer = StringField("Composer", [validators.required(), validators.length(min=3, max=50)])
    arranger = StringField("Arranger", [validators.required(), validators.length(min=3, max=50)])
    style = StringField("Style", [validators.required(), validators.length(min=3, max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        piece = Piece.query.filter_by(name=name.data).first()
        if piece is not None:
            raise ValidationError("This piece already exists in the database.")

# rivin haku (kesken)
class SearchForm(FlaskForm):
    name = StringField("Piece name")
    composer = StringField("Composer")
    arranger = StringField("Arranger")
    style = StringField("Style")

    class Meta:
        csrf = False

# rivin muokkaus (kesken)
class EditForm(FlaskForm):
    technique = StringField("Special technique", [validators.required(), validators.length(min=3, max=50)])

class DeleteForm(FlaskForm):
    delete = BooleanField("Delete row")

    class Meta:
        csrf = False
