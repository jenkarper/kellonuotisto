from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.pieces.models import Piece
from application.supplements.models import Arranger, Composer, Style, Technique
from application.supplements.forms import ArrangerForm, ComposerForm, DeleteForm, EditForm, StyleForm, TechniqueForm

# ARRANGERS
@app.route("/arrangers", methods=["GET"])
def arrangers_index():
    return render_template("arrangers/list.html", arrangers = Arranger.query.all())

@app.route("/arrrangers/<arranger_id>/")
def arrangers_show(arranger_id):
    arranger = Arranger.query.get(arranger_id)
    return render_template("arrangers/show.html", arranger = arranger)

@app.route("/arrangers/new/")
@login_required
def arrangers_form():
    return render_template("arrangers/new.html", form = ArrangerForm())

@app.route("/arrangers/", methods=["POST"])
@login_required
def arrangers_create():
    form = ArrangerForm(request.form)

    if not form.validate():
        return render_template("arrangers/new.html", form = form)
    
    a = Arranger(form.name.data)

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("arrangers_index"))

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

    return "Deleted successfully!"

# COMPOSERS
@app.route("/composers/", methods=["GET"])
def composers_index():
    return render_template("composers/list.html", composers = Composer.query.all(), form = EditForm)

@app.route("/composers/<composer_id>/")
def composers_show(composer_id):
    composer = Composer.query.get(composer_id)
    return render_template("composers/show.html", composer = composer)

@app.route("/composers/new/")
@login_required
def composers_form():
    return render_template("composers/new.html", form = ComposerForm())

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

    return "Deleted successfully!"

@app.route("/composers/", methods=["POST"])
@login_required
def composers_create():
    form = ComposerForm(request.form)

    if not form.validate():
        return render_template("composers/new.html", form = form)

    c = Composer(form.name.data)

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("composers_index"))

# STYLES
@app.route("/styles", methods=["GET"])
def styles_index():
    return render_template("styles/list.html", styles = Style.query.all())

@app.route("/styles/new/")
@login_required
def styles_form():
    return render_template("styles/new.html", form = StyleForm())

@app.route("/styles/", methods=["POST"])
@login_required
def styles_create():
    form = StyleForm(request.form)

    if not form.validate():
        return render_template("styles/new.html", form = form)

    s = Style(form.name.data)

    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("styles_index"))

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

    return "Deleted successfully!"

# TECHNIQUES
@app.route("/techniques", methods=["GET"])
def techniques_index():
    return render_template("techniques/list.html", techniques = Technique.query.all())

@app.route("/techniques/new/")
@login_required
def techniques_form():
    return render_template("techniques/new.html", form = TechniqueForm())

@app.route("/techniques/", methods=["POST"])
@login_required
def techniques_create():
    form = TechniqueForm(request.form)

    if not form.validate():
        return render_template("techniques/new.html", form = form)

    t = Technique(form.name.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("techniques_index"))

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
