from application import db
from application.models import Base

piece_concert = db.Table('piece_concert',
    db.Column('piece_id', db.Integer, db.ForeignKey('piece.id')),
    db.Column('concert_id', db.Integer, db.ForeignKey('concert.id'))
)

class Concert(Base):
    venue = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(), nullable=False)

    def __init__(self, name, venue, date):
        self.name = name
        self.venue = venue
        self.date = date

