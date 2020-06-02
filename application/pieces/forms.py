from application import app
from application.pieces.models import Piece

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, SubmitField, validators
from wtforms.validators import ValidationError

Bootstrap(app)

# uuden rivin luonti
class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    composer_list = StringField("Existing composer")
    composer_new = StringField("New Composer", [validators.length(max=50)])
    arranger = StringField("Arranger", [validators.required(), validators.length(min=3, max=50)])
    style = StringField("Style", [validators.required(), validators.length(min=3, max=50)])
    submit = SubmitField('Submit')
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        piece = Piece.query.filter_by(name=name.data).first()
        if piece is not None:
            raise ValidationError("This piece already exists in the database.")

# rivin muokkaus (kesken)
class EditForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")

# rivin haku
class SearchForm(FlaskForm):
    name = StringField("Piece name")
    composer = StringField("Composer name")
    arranger = StringField("Arranger name")
    style = StringField("Style name")

    class Meta:
        csrf = False

# rivin poisto
class DeleteForm(FlaskForm):
    delete = BooleanField("Delete row")

    class Meta:
        csrf = False

# konsertin lisäys
class ProgrammeForm(FlaskForm):
    concert_id = IntegerField("Concert id")

    class Meta:
        csrf = False

