from application import db
from application.models import Base
from application.supplements.models import piece_technique, Technique
from application.concerts.models import piece_concert, Concert

from sqlalchemy.sql import text

class Piece(Base):

    octaves = db.Column(db.String(150), nullable=False)
    length = db.Column(db.Integer, nullable=False)

    composer_id = db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    arranger_id = db.Column(db.Integer, db.ForeignKey('arranger.id'), nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'), nullable=False)

    techniques = db.relationship('Technique', secondary=piece_technique, backref=db.backref('pieces', lazy=True))
    concerts = db.relationship('Concert', secondary=piece_concert, backref=db.backref('pieces', lazy=True))

    def __init__(self, name, octaves, length, composer_id, arranger_id, style_id):
        self.name = name
        self.octaves = octaves
        self.length = length
        self.composer_id = composer_id
        self.arranger_id = arranger_id
        self.style_id = style_id

    @staticmethod
    def count_pieces_by_style():
        stmt = text("SELECT Style.name, COUNT(*), SUM(length)"
                    " FROM Piece"
                    " LEFT JOIN Style ON Style.id = Piece.style_id"
                    " GROUP BY Style.name"
                    " ORDER BY Style.name")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"style":row[0], "pieces":row[1], "minutes":row[2]})

        return response

    @staticmethod
    def find_music(word):
        stmt = text ("SELECT Piece.name, Piece.id FROM Piece"
                     " JOIN Style ON Style.id = Piece.style_id"
                     " JOIN Composer ON Composer.id = Piece.composer_id"
                     " JOIN Arranger ON Arranger.id = Piece.arranger_id"
                     " WHERE LOWER(Piece.name) LIKE LOWER(:word)"
                     " OR LOWER(Style.name) LIKE LOWER(:word)"
                     " OR LOWER(Composer.name) LIKE LOWER(:word)"
                     " OR LOWER(Arranger.name) LIKE LOWER(:word)").params(word='%'+word+'%')

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "id":row[1]})

        return response

    @staticmethod
    def find_piece_by_style(style_id):
        stmt = text ("SELECT Piece.name FROM Piece"
                     " WHERE Piece.style_id = :style_id").params(style_id=style_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response

