from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, validators

class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    composer = StringField("Composer")
    arranger = StringField("Arranger")
    style = StringField("Style")
 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    name = StringField("Piece name")
    composer = StringField("Composer")
    arranger = StringField("Arranger")
    style = StringField("Style")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    newname = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    newoctaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    newlength = IntegerField("Length (in minutes)")
