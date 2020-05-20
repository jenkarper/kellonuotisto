from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class PieceForm(FlaskForm):
    name = StringField("Piece name")
    octaves = StringField("Used octaves")
    length = IntegerField("Length (in minutes)")
 
    class Meta:
        csrf = False

