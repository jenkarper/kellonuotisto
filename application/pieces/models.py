from application import db

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(50), nullable=False)
    octaves = db.Column(db.String(150), nullable=False)
    length = db.Column(db.Integer, nullable=False)

    composer_id = db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    arranger_id = db.Column(db.Integer, db.ForeignKey('arranger.id'), nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'), nullable=False)

    def __init__(self, name, octaves, length, composer_id, arranger_id, style_id):
        self.name = name
        self.octaves = octaves
        self.length = length
        self.composer_id = composer_id
        self.arranger_id = arranger_id
        self.style_id = style_id

