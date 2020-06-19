from flask import flash, redirect, render_template, request, url_for

from application import app, db, login_required
from application.pieces.models import Piece
from application.supplements.models import Arranger, Composer, Style, Technique
from application.supplements.forms import DeleteForm, EditForm, TechniqueForm

# ARRANGERS
# Palauttaa listanäkymän sovittajista
@app.route("/arrangers", methods=["GET"])
def arrangers_index():
    arrangers = db.session.query(Arranger).order_by(Arranger.name)
    return render_template("arrangers/list.html", arrangers = arrangers)

# Näyttää yhden sovittajan tiedot
@app.route("/arrrangers/<arranger_id>/")
def arrangers_show(arranger_id):
    arranger = Arranger.query.get(arranger_id)
    return render_template("arrangers/show.html", arranger = arranger)

# Muokkaa yhden sovittajan tietoja
@app.route("/arrangers/edit/<arranger_id>", methods=["GET", "POST"])
@login_required
def arrangers_edit(arranger_id):
    arranger = Arranger.query.get(arranger_id)

    if request.method == "GET":
        return render_template("arrangers/edit.html", form = EditForm(), arranger_id = arranger_id, arranger = arranger)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("arrangers/edit.html", form = form, arranger_id = arranger_id, arranger = arranger)

    name = request.form["newname"]
    arranger.name = name
    db.session().commit()

    return redirect(url_for("arrangers_index"))

# Poistaa yhden sovittajan tiedot
@app.route("/arrangers/delete/<arranger_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def arrangers_delete(arranger_id):

    if request.method == "GET":
        arranger = Arranger.query.get(arranger_id)
        return render_template("arrangers/delete.html", form = DeleteForm(), arranger_id = arranger_id, arranger = arranger)

    form = DeleteForm(request.form)

    a = Arranger.query.get(arranger_id)

    for piece in a.pieces:
        if piece.arranger_id == a.id:
            return render_template("failure.html")
    
    db.session().delete(a)
    db.session().commit()

    return render_template("success.html")

# COMPOSERS
@app.route("/composers/", methods=["GET"])
def composers_index():
    composers = db.session.query(Composer).order_by(Composer.name)
    return render_template("composers/list.html", composers = composers, form = EditForm)

@app.route("/composers/<composer_id>/")
def composers_show(composer_id):
    composer = Composer.query.get(composer_id)
    return render_template("composers/show.html", composer = composer)

@app.route("/composers/edit/<composer_id>", methods=["GET", "POST"])
@login_required
def composers_edit(composer_id):
    composer = Composer.query.get(composer_id)

    if request.method == "GET":
        return render_template("composers/edit.html", form = EditForm(), composer_id = composer_id, composer = composer)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("composers/edit.html", form = form, composer_id = composer_id, composer = composer)

    name = request.form["newname"]
    composer.name = name
    db.session().commit()

    return redirect(url_for("composers_index"))

@app.route("/composers/delete/<composer_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def composers_delete(composer_id):

    if request.method == "GET":
        composer = Composer.query.get(composer_id)
        return render_template("composers/delete.html", form = DeleteForm(), composer_id=composer_id, composer = composer)

    form = DeleteForm(request.form)

    c = Composer.query.get(composer_id)

    for piece in c.pieces:
        if piece.composer_id == c.id:
            return render_template("failure.html")
    
    db.session().delete(c)
    db.session().commit()

    return render_template("success.html")

# STYLES
@app.route("/styles", methods=["GET"])
def styles_index():
    styles = db.session.query(Style).order_by(Style.name)
    return render_template("styles/list.html", styles = styles)

@app.route("/styles/edit/<style_id>", methods=["GET", "POST"])
@login_required
def styles_edit(style_id):

    if request.method == "GET":
        style = Style.query.get(style_id)
        return render_template("styles/edit.html", form = EditForm(), style_id = style_id, style = style)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("styles/edit.html", form = form, style_id = style_id, style = style)

    s = Style.query.get(style_id)
    s.name = request.form["newname"]
    db.session().commit()

    return redirect(url_for("styles_index"))

@app.route("/styles/delete/<style_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def styles_delete(style_id):
    style = Style.query.get(style_id)

    if request.method == "GET":
        return render_template("styles/delete.html", form = DeleteForm(), style_id = style_id, style = style)

    form = DeleteForm(request.form)
    # Toteutin tyylilajin poistamisen ensin samalla tavoin kuin säveltäjän ja sovittajan, mutta se ei jostain syystä toiminut...?
    pieces = Piece.find_piece_by_style(style_id)
    if len(pieces) != 0:
        return render_template("failure.html")
  
    db.session().delete(style)
    db.session().commit()

    return render_template("success.html")

# TECHNIQUES
@app.route("/techniques", methods=["GET"])
def techniques_index():
    techniques = db.session.query(Technique).order_by(Technique.name)
    return render_template("techniques/list.html", techniques = techniques)

@app.route("/pieces/techniques/<piece_id>", methods=["GET", "POST"])
@login_required
def techniques_create(piece_id):
    piece = Piece.query.get(piece_id)
    techniques = db.session.query(Technique).order_by(Technique.name)
    technique_names = [t.name for t in techniques]

    if request.method == "GET":
        return render_template("techniques/new.html", form = TechniqueForm(), piece = piece, piece_id = piece_id, techniques = technique_names)

    form = TechniqueForm(request.form)

    if not form.validate():
        return render_template("techniques/new.html", form = form, piece = piece, piece_id = piece_id, techniques = technique_names)

    # tarkistetaan, onko erikoistekniikka jo tietokannassa vai luodaanko uusi

    t = Technique.query.filter_by(name=request.form.get("name")).first()
    if t is None:
        t = Technique(request.form.get("name"))
        db.session().add(t)
        db.session().flush()

    piece.techniques.append(t)
    
    db.session().commit()

    return redirect(url_for("pieces_show", piece_id=piece_id))

@app.route("/techniques/edit/<technique_id>", methods=["GET", "POST"])
@login_required
def techniques_edit(technique_id):

    if request.method == "GET":
        tech = Technique.query.get(technique_id)
        return render_template("techniques/edit.html", form = EditForm(), technique_id=technique_id, tech = tech)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("techniques/edit.html", form = form, technique_id=technique_id, tech = tech)

    t = Technique.query.get(technique_id)
    t.name = request.form["newname"]
    db.session().commit()

    return redirect(url_for("techniques_index"))

@app.route("/techniques/delete/<technique_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def techniques_delete(technique_id):

    if request.method == "GET":
        technique = Technique.query.get(technique_id)
        return render_template("techniques/delete.html", form = DeleteForm(), technique_id = technique_id, tech = technique)

    form = DeleteForm(request.form)

    t = Technique.query.get(technique_id)

    if t.pieces is not None:
        return render_template("failure.html")
    
    db.session().delete(t)
    db.session().commit()

    return render_template("success.html")
