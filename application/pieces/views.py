from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.pieces.models import Piece
from application.pieces.forms import EditForm, DeleteForm, PieceForm, ProgrammeForm, SearchForm
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
    techniques = db.session().query(Technique).order_by(Technique.name)
    technique_names = [t.name for t in techniques]
    return render_template("techniques/new.html", form = TechniqueForm(), piece = piece, piece_id = piece_id, techniques = technique_names)

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
    concerts = db.session.query(Concert).order_by(Concert.date)

    if request.method == "GET":
        return render_template("pieces/concerts.html", form = ProgrammeForm(), piece = piece, concerts = concerts)

    form = ProgrammeForm(request.form)
    concert_name = request.form["concert_listed"]
    concert = Concert.query.filter_by(name=concert_name).first()

    piece.concerts.append(concert)
    db.session().commit()

    return redirect(url_for("pieces_show", piece_id=piece_id))

# Muokkaa kappaleen tietoja
@app.route("/pieces/edit/<piece_id>", methods = ["GET", "POST"])
@login_required
def pieces_edit(piece_id):
    piece = Piece.query.get(piece_id)

    if request.method == "GET":
        return render_template("pieces/edit.html", form = EditForm(), piece = piece, piece_id = piece_id)

    form = EditForm(request.form)
    newname = request.form["newname"]
    newoctaves = request.form["newoctaves"]
    newlength = request.form["newlength"]

    piece.name = newname
    piece.octaves = newoctaves
    piece.length = newlength

    db.session().commit()

    return redirect(url_for("pieces_show", piece_id=piece_id))

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
    composers = db.session.query(Composer).order_by(Composer.name)
    composer_names = [c.name for c in composers]
    arrangers = db.session.query(Arranger).order_by(Arranger.name)
    arranger_names = [a.name for a in arrangers]
    styles = db.session.query(Style).order_by(Style.name)
    style_names = [s.name for s in styles]

    return render_template("pieces/new.html", form = PieceForm(), composers = composer_names, arrangers = arranger_names, styles = style_names)

# Lisää uuden kappaleen (tarvittaessa myös säveltäjän, sovittajan ja tyylilajin)
@app.route("/pieces/", methods = ["POST"])
@login_required
def pieces_create():
    composers = db.session.query(Composer).order_by(Composer.name)
    composer_names = [c.name for c in composers]
    arrangers = db.session.query(Arranger).order_by(Arranger.name)
    arranger_names = [a.name for a in arrangers]
    styles = db.session.query(Style).order_by(Style.name)
    style_names = [s.name for s in styles]
    form = PieceForm(request.form)

    if not form.validate():
        return render_template("pieces/new.html", form = form, composers = composer_names, arrangers = arranger_names, styles = style_names)

    name = request.form["name"]
    octaves = request.form["octaves"]
    length = request.form["length"]

    # tarkistetaan, onko säveltäjä jo tietokannassa vai luodaanko uusi

    composer = Composer.query.filter_by(name=request.form.get("composer")).first()
    if composer is None:
        composer = Composer(request.form.get("composer"))
        db.session().add(composer)
        db.session().flush()

    # tarkistetaan, onko sovittaja jo tietokannassa vai luodaanko uusi

    arranger = Arranger.query.filter_by(name=request.form.get("arranger")).first()
    if arranger is None:
        arranger = Arranger(request.form.get("arranger"))
        db.session().add(arranger)
        db.session().flush()

    # tarkistetaan, onko tyylilaji jo tietokannassa vai luodaanko uusi

    style = Style.query.filter_by(name=request.form.get("style")).first()
    if style is None:
        style = Style(request.form.get("style"))
        db.session().add(style)
        db.session().flush()

    # luodaan uusi rivi tauluun Piece
    p = Piece(name, octaves, length, composer.id, arranger.id, style.id)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pieces_index"))

# Hakee tietoa taulusta Piece
@app.route("/pieces/search/", methods = ["GET", "POST"])
@login_required
def pieces_search():

    if request.method == "GET":
        return render_template("pieces/search.html", form = SearchForm())
    
    form = SearchForm(request.form)
    word = request.form.get("searchword")
    
    pieces = Piece.find_music(word)

    return render_template("pieces/results.html", pieces = pieces, word = word)

