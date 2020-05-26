from application import db
from application.models import Base
from application.supplements.models import piece_technique, Technique

class Piece(Base):

    octaves = db.Column(db.String(150), nullable=False)
    length = db.Column(db.Integer, nullable=False)

    composer_id = db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    arranger_id = db.Column(db.Integer, db.ForeignKey('arranger.id'), nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'), nullable=False)

    techniques = db.relationship('Technique', secondary=piece_technique, backref=db.backref('pieces'))

    def __init__(self, name, octaves, length, composer_id, arranger_id, style_id):
        self.name = name
        self.octaves = octaves
        self.length = length
        self.composer_id = composer_id
        self.arranger_id = arranger_id
        self.style_id = style_id
