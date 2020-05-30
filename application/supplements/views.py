from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.pieces.models import Piece
from application.supplements.models import Arranger, Composer, Style, Technique
from application.supplements.forms import DeleteForm, EditForm, TechniqueForm

# ARRANGERS
# Palauttaa listanäkymän sovittajista
@app.route("/arrangers", methods=["GET"])
def arrangers_index():
    return render_template("arrangers/list.html", arrangers = Arranger.query.all())

# Näyttää yhden sovittajan tiedot
@app.route("/arrrangers/<arranger_id>/")
def arrangers_show(arranger_id):
    arranger = Arranger.query.get(arranger_id)
    return render_template("arrangers/show.html", arranger = arranger)

# Muokkaa yhden sovittajan tietoja
@app.route("/arrangers/edit/<arranger_id>", methods=["GET", "POST"])
@login_required
def arrangers_edit(arranger_id):

    if request.method == "GET":
        arranger = Arranger.query.get(arranger_id)
        return render_template("arrangers/edit.html", form = EditForm(), arranger_id=arranger_id, arranger=arranger)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("arrangers/edit.html", form = form, arranger_id=arranger_id, arranger=arranger)

    a = Arranger.query.get(arranger_id)
    a.name = form.newname.data
    db.session().commit()

    return redirect(url_for("arrangers_index"))

# Poistaa yhden sovittajan tiedot
@app.route("/arrangers/delete/<arranger_id>", methods=["GET", "POST"])
@login_required
def arrangers_delete(arranger_id):

    if request.method == "GET":
        arranger = Arranger.query.get(arranger_id)
        return render_template("arrangers/delete.html", form = DeleteForm(), arranger_id=arranger_id, arranger=arranger)

    form = DeleteForm(request.form)

    a = Arranger.query.get(arranger_id)

    for piece in a.pieces:
        if piece.composer_id == a.id:
            return "This arranger is referred to in another table and cannot be deleted!"
    
    db.session().delete(a)
    db.session().commit()

    return render_template("success.html")

# COMPOSERS
@app.route("/composers/", methods=["GET"])
def composers_index():
    return render_template("composers/list.html", composers = Composer.query.all(), form = EditForm)

@app.route("/composers/<composer_id>/")
def composers_show(composer_id):
    composer = Composer.query.get(composer_id)
    return render_template("composers/show.html", composer = composer)

@app.route("/composers/edit/<composer_id>", methods=["GET", "POST"])
@login_required
def composers_edit(composer_id):

    if request.method == "GET":
        composer = Composer.query.get(composer_id)
        return render_template("composers/edit.html", form = EditForm(), composer_id = composer_id, composer = composer)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("composers/edit.html", form = form, composer_id = composer_id, composer = composer)

    c = Composer.query.get(composer_id)
    c.name = form.newname.data
    db.session().commit()

    return redirect(url_for("composers_index"))

@app.route("/composers/delete/<composer_id>", methods=["GET", "POST"])
@login_required
def composers_delete(composer_id):

    if request.method == "GET":
        composer = Composer.query.get(composer_id)
        return render_template("composers/delete.html", form = DeleteForm(), composer_id=composer_id, composer = composer)

    form = DeleteForm(request.form)

    c = Composer.query.get(composer_id)

    for piece in c.pieces:
        if piece.composer_id == c.id:
            return "This composer is referred to in another table and cannot be deleted!"
    
    db.session().delete(c)
    db.session().commit()

    return render_template("success.html")

# STYLES
@app.route("/styles", methods=["GET"])
def styles_index():
    return render_template("styles/list.html", styles = Style.query.all())

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
    s.name = form.newname.data
    db.session().commit()

    return redirect(url_for("styles_index"))

@app.route("/styles/delete/<style_id>", methods=["GET", "POST"])
@login_required
def styles_delete(style_id):

    if request.method == "GET":
        style = Style.query.get(style_id)
        return render_template("styles/delete.html", form = DeleteForm(), style_id = style_id, style = style)

    form = DeleteForm(request.form)

    s = Style.query.get(style_id)

    for piece in s.pieces:
        if piece.style_id == s.id:
            return "This style is referred to in another table and cannot be deleted!"
    
    db.session().delete(s)
    db.session().commit()

    return render_template("success.html")

# TECHNIQUES
@app.route("/techniques", methods=["GET"])
def techniques_index():
    return render_template("techniques/list.html", techniques = Technique.query.all())

@app.route("/pieces/techniques/<piece_id>", methods=["GET", "POST"])
@login_required
def techniques_create(piece_id):
    piece = Piece.query.get(piece_id)

    if request.method == "GET":
        return render_template("techniques/new.html", form = TechniqueForm(), piece = piece, piece_id = piece_id)

    form = TechniqueForm(request.form)

    if not form.validate():
        return render_template("techniques/new.html", form = form, piece = piece, piece_id = piece_id)

    technique = form.name.data
    t = Technique(technique)

    # tarkistetaan, onko erikoistekniikka jo tietokannassa

    t = Technique.query.filter_by(name=form.name.data).first()

    if t is None:
        t = Technique(technique)
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
    t.name = form.newname.data
    db.session().commit()

    return redirect(url_for("techniques_index"))
