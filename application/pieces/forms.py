from application import app
from application.pieces.models import Piece

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, SubmitField, validators
from wtforms.validators import ValidationError

# uuden rivin luonti
class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    composer = StringField("Composers", [validators.required(), validators.length(min=5, max=50)])
    arranger = StringField("Arranger", [validators.required(), validators.length(min=5, max=50)])
    style = StringField("Style", [validators.required(), validators.length(min=5, max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        piece = Piece.query.filter_by(name=name.data).first()
        if piece is not None:
            raise ValidationError("Tämän niminen kappale on jo tietokannassa.")

# rivin muokkaus
class EditForm(FlaskForm):
    newname = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    newoctaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    newlength = IntegerField("Length (in minutes)")

# rivin haku
class SearchForm(FlaskForm):
    searchword = StringField("Search word", [validators.required(), validators.length(max=20)])

    class Meta:
        csrf = False

# rivin poisto
class DeleteForm(FlaskForm):
    delete = BooleanField("Delete row")

    class Meta:
        csrf = False

# konsertin lisäys
class ProgrammeForm(FlaskForm):
    concert_listed = StringField("Concert name", [validators.required(), validators.length(min=5, max=50)])

    class Meta:
        csrf = False

