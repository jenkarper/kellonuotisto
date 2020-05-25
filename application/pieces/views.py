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
    composer = form.composer.data
    arranger = form.arranger.data
    style = form.style.data

    # tarkistetaan, ovatko säveltäjä, sovittaja ja tyyli jo tietokannassa

    c = Composer.query.filter_by(name=composer).first()
    a = Arranger.query.filter_by(name=arranger).first()
    s = Style.query.filter_by(name=style).first()
    
    if c is None:
        c = Composer(composer)
        db.session().add(c)
        db.session().flush()

    if a is None:
        a = Arranger(arranger)
        db.session().add(a)
        db.session().flush()

    if s is None:
        s = Style(style)
        db.session().add(s)
        db.session().flush()

    composer_id = c.id
    arranger_id = a.id
    style_id = s.id

    p = Piece(name, octaves, length, composer_id, arranger_id, style_id)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pieces_index"))

