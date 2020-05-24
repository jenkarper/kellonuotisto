from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.pieces.models import Piece
from application.pieces.forms import PieceForm

from application.supplements.models import Composer

@app.route("/pieces", methods=["GET"])
def pieces_index():
    return render_template("pieces/list.html", pieces = Piece.query.all())

@app.route("/pieces/new/")
@login_required
def pieces_form():
    return render_template("pieces/new.html", form = PieceForm())

@app.route("/pieces/", methods=["POST"])
@login_required
def pieces_create():
    form = PieceForm(request.form)

    if not form.validate():
        return render_template("pieces/new.html", form = form)

    name = form.name.data
    octaves = form.octaves.data
    length = form.length.data

    p = Piece(name, octaves, length)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pieces_index"))

