from application import db
from application.models import Base
#from application.pieces.models import Piece

piece_technique = db.Table('piece_technique',
    db.Column('piece_id', db.Integer, db.ForeignKey('piece.id')),
    db.Column('technique_id', db.Integer, db.ForeignKey('technique.id'))
    )

class Arranger(Base):
    pieces = db.relationship('Piece', backref='arranger', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Composer(Base):
    pieces = db.relationship('Piece', backref='composer', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Style(Base):
    pieces = db.relationship('Piece', backref='style', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Technique(Base):
    def __init__(self, name):
        self.name = name
