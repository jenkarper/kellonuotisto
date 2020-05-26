from application import db
#from application.pieces.models import Piece

piece_technique = db.Table('piece_technique',
    db.Column('piece_id', db.Integer, db.ForeignKey('piece.id')),
    db.Column('technique_id', db.Integer, db.ForeignKey('technique.id'))
    )

class Arranger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    pieces = db.relationship('Piece', backref='arranger', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Composer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    pieces = db.relationship('Piece', backref='composer', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Style(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    pieces = db.relationship('Piece', backref='style', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Technique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
