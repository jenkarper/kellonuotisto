from application import db
from application.models import Base

from sqlalchemy.sql import text

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

    @staticmethod
    def list_concerts():
        stmt = text ("SELECT Concert.name, COUNT(*) FROM piece_concert"
                     " JOIN Concert ON Concert.id = piece_concert.concert_id"
                     " GROUP BY Concert.name"
                     " ORDER BY Concert.date")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "pieces":row[1]})

        return response

