from application import db

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(50), nullable=False)
    octaves = db.Column(db.String(150), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    last_concert = db.Column(db.String(150), nullable=True)

    def __init__(self, name, octaves, length):
        self.name = name
        self.octaves = octaves
        self.length = length

