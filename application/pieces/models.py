from application import db
from application.models import Base
from application.supplements.models import piece_technique, Technique

from sqlalchemy.sql import text

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

    @staticmethod
    def find_music_by_style():
        stmt = text("SELECT Style.name, COUNT(*), SUM(length)"
                    " FROM Piece"
                    " LEFT JOIN Style ON Style.id = Piece.style_id"
                    " GROUP BY Style.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"style":row[0], "pieces":row[1], "minutes":row[2]})
            #print(row[0])
            #print(row[1])
            #print(row[2])

    @staticmethod
    def find_music_by_composer(name):
        stmt = text("SELECT Piece.name FROM Piece"
                    " JOIN Composer ON Composer.id = Piece.composer_id"
                    " WHERE Composer.name = :name").params(name=name)

        res = db.engine.execute(stmt)

        for row in res:
            print(row[0])
