from application import db
from application.models import Base
from application.pieces.models import Piece
from application.concerts.models import Concert
from werkzeug.security import check_password_hash

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account" # koska 'user' on varattu avainsana PostgreSQL:ssä
  
    username = db.Column(db.String(144), nullable=False)
    password_hash = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password_hash, role):
        self.name = name
        self.username = username
        self.password_hash = password_hash
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_role(self):
        return self.role

    def is_admin(self):
        return self.role == "ADMIN"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    comment = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    piece_id = db.Column(db.Integer, db.ForeignKey('piece.id'), nullable=True)
    piece_name = db.Column(db.String(144), nullable=False)

    def __init__(self, comment, user_id, piece_id, piece_name):
        self.comment = comment
        self.user_id = user_id
        self.piece_id = piece_id
        self.piece_name = piece_name

    @staticmethod
    def search_notes_by_piece_and_user(user_id, piece_id):
        stmt = text("SELECT comment FROM Note"
                    " WHERE user_id = :user_id"
                    " AND piece_id = :piece_id").params(user_id=user_id, piece_id=piece_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"comment":row[0]})

        return response

