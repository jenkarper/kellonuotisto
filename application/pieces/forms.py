from application import app
from application.pieces.models import Piece

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, SubmitField, validators
from wtforms.validators import ValidationError

#Bootstrap(app)

# uuden rivin luonti
class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    composer_list = StringField("Existing composer")
    composer_new = StringField("New Composer", [validators.length(max=50)])
    arranger_list = StringField("Existing arranger")
    arranger_new = StringField("New arranger", [validators.length(max=50)])
    style_list = StringField("Existing style")
    style_new = StringField("New style", [validators.length(max=50)])
 
    class Meta:
        csrf = False

    def validate_name(self, name):
        piece = Piece.query.filter_by(name=name.data).first()
        if piece is not None:
            raise ValidationError("Tämän niminen kappale on jo tietokannassa.")

    #def validate_composer(self, composer_list, composer_new):
    #    composer_list = composer_list.data
    #    composer_new = composer_new.data
    #    if composer is None:
    #        if composer_new is None:            
    #            raise ValidationError("Säveltäjää ei voi jättää tyhjäksi!")

# rivin muokkaus (kesken)
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
    concert_listed = StringField("Concert name")

    class Meta:
        csrf = False

