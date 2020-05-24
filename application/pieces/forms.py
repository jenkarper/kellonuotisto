from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PieceForm(FlaskForm):
    name = StringField("Piece name", [validators.required(), validators.length(min=5, max=50)])
    octaves = StringField("Used octaves", [validators.required(), validators.length(min=1, max=20)])
    length = IntegerField("Length (in minutes)")
    #composer_id = IntegerField("Composer")
 
    class Meta:
        csrf = False

