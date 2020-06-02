from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.pieces.models import Piece
from application.pieces.forms import DeleteForm, PieceForm, ProgrammeForm, SearchForm
from application.auth.forms import NoteForm
from application.supplements.forms import TechniqueForm

from application.supplements.models import Composer, Arranger, Style, Technique
from application.auth.models import Note
from application.concerts.models import Concert

# Näyttää tietokannassa olevat kappaleet listana
@app.route("/pieces", methods = ["GET"])
def pieces_index():
    pieces = db.session.query(Piece).order_by(Piece.name)
    return render_template("pieces/list.html", pieces = pieces, pieces_by_style = Piece.count_pieces_by_style())

# Näyttää yhden kappaleen tiedot
@app.route("/pieces/<piece_id>/")
def pieces_show(piece_id):
    user_id = current_user.id
    notes = Note.search_notes_by_piece_and_user(user_id, piece_id)
    return render_template("pieces/show.html", piece = Piece.query.get(piece_id), notes = notes)

# Palauttaa erikoistekniikan lisäyslomakkeen
@app.route("/pieces/techniques/<piece_id>/")
@login_required
def pieces_techniques(piece_id):
    piece = Piece.query.get(piece_id)
    return render_template("techniques/new.html", form = TechniqueForm(), piece = piece, piece_id = piece_id)

# Palauttaa muistiinpanon lisäyslomakkeen
@app.route("/pieces/notes/<piece_id>/")
@login_required(role="ADMIN")
def pieces_notes(piece_id):
    piece = Piece.query.get(piece_id)
    return render_template("notes/new.html", form = NoteForm(), piece = piece, piece_id = piece_id)

# Liittää olemassaolevan konsertin kappaleeseen
@app.route("/pieces/concerts/<piece_id>", methods = ["GET", "POST"])
@login_required(role="ADMIN")
def pieces_concerts(piece_id):
    piece = Piece.query.get(piece_id)
    concerts = Concert.query.all()

    if request.method == "GET":
        return render_template("pieces/concerts.html", form = ProgrammeForm(), piece = piece, concerts = concerts)

    form = ProgrammeForm(request.form)
    concert = Concert.query.get(request.form["concert_id"])

    if concert is not None:
        piece.concerts.append(concert)
        db.session().commit()

        return redirect(url_for("pieces_show", piece_id=piece_id))

    else:
        return "Tarkista syöttämäsi konsertin tunniste!"

# Muokkaa kappaleen tietoja
@app.route("/pieces/edit/<piece_id>", methods = ["GET", "POST"])
@login_required
def pieces_edit(piece_id):
    piece = Piece.query.get(piece_id)
    return render_template("pieces/edit.html", piece = piece, piece_id = piece_id)

# Poistaa kappaleen
@app.route("/pieces/delete/<piece_id>", methods = ["GET", "POST"])
@login_required(role="ADMIN")
def pieces_delete(piece_id):

    if request.method == "GET":
        piece = Piece.query.get(piece_id)
        return render_template("pieces/delete.html", form = DeleteForm(), piece_id = piece_id, piece = piece)

    p = Piece.query.get(piece_id)

    db.session().delete(p)
    db.session().commit()
    
    return render_template("success.html")

# Palauttaa kappaleen lisäyslomakkeen
@app.route("/pieces/new/")
@login_required
def pieces_form():
    composers = Composer.query.all()
    return render_template("pieces/new.html", form = PieceForm(), composers = composers)

# Lisää uuden kappaleen (tarvittaessa myös säveltäjän, sovittajan ja tyylilajin)
@app.route("/pieces/", methods = ["POST"])
@login_required
def pieces_create():
    form = PieceForm(request.form)

    if not form.validate():
        return render_template("pieces/new.html", form = form)

    name = request.form["name"]
    octaves = request.form["octaves"]
    length = request.form["length"]

    composer = request.form.get("composer_list")
    
    if composer is None:
        composer = Composer(request.form["composer_new"])
        db.session().add(composer)
        db.session().flush()
    else:
        composer = Composer.query.filter_by(name=composer).first()

    arranger = request.form["arranger"]
    style = request.form["style"]

    # tarkistetaan, ovatko säveltäjä, sovittaja ja tyyli jo tietokannassa

    #c = Composer.query.filter_by(name=composer).first()
    a = Arranger.query.filter_by(name=arranger).first()
    s = Style.query.filter_by(name=style).first()
    
   # if c is None:
    #    c = Composer(composer)
     #   db.session().add(c)
      #  db.session().flush()

    if a is None:
        a = Arranger(arranger)
        db.session().add(a)
        db.session().flush()

    if s is None:
        s = Style(style)
        db.session().add(s)
        db.session().flush()

    #composer_id = c.id
    arranger_id = a.id
    style_id = s.id

    p = Piece(name, octaves, length, composer.id, arranger_id, style_id)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pieces_index"))

# Hakee tietoa taulusta Piece
@app.route("/pieces/search/", methods = ["GET", "POST"])
@login_required
def pieces_search():

    if request.method == "GET":
        pieces = Piece.query.all()
        return render_template("pieces/search.html", form = SearchForm(), pieces = pieces)
    
    form = SearchForm(request.form)
    name = request.form["name"]
    composer = request.form["composer"]
    arranger = request.form["arranger"]
    style = request.form["style"]

    p = Piece.query.filter_by(name=name).first()
    c = Composer.query.filter_by(name=composer).first()
    a = Arranger.query.filter_by(name=arranger).first()
    s = Style.query.filter_by(name=style).first()

    if p is not None:
        return render_template("pieces/show.html", piece = p)

    elif c is not None:
        return render_template("composers/show.html", composer = c)

    elif a is not None:
        return render_template("arrangers/show.html", arranger = a)

    elif s is not None:
        return render_template("styles/show.html", style = s)

    else:
        return "Annetuilla tiedoilla ei löydy yhtään musiikkia tietokannasta!"
