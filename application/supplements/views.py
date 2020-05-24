from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.supplements.models import Arranger, Composer, Style, Technique
from application.supplements.forms import ArrangerForm, ComposerForm, StyleForm, TechniqueForm, ModifyForm

# ARRANGERS
@app.route("/arrangers", methods=["GET"])
def arrangers_index():
    return render_template("arrangers/list.html", arrangers = Arranger.query.all())

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

@app.route("/arrangers/modify/<arranger_id>", methods=["GET", "POST"])
@login_required
def arrangers_modify(arranger_id):

    if request.method == "GET":
        return render_template("arrangers/modify.html", form = ModifyForm(), arranger_id=arranger_id)

    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("arrangers/modify.html", form = form, arranger_id=arranger_id)

    a = Arranger.query.get(arranger_id)
    a.name = form.newname.data
    db.session().commit()

    return redirect(url_for("arrangers_index"))

# COMPOSERS
@app.route("/composers/", methods=["GET"])
def composers_index():
    return render_template("composers/list.html", composers = Composer.query.all(), form = ModifyForm)

@app.route("/composers/new/")
@login_required
def composers_form():
    return render_template("composers/new.html", form = ComposerForm())

@app.route("/composers/modify/<composer_id>", methods=["GET", "POST"])
@login_required
def composers_modify(composer_id):

    if request.method == "GET":
        return render_template("composers/modify.html", form = ModifyForm(), composer_id=composer_id)

    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("composers/modify.html", form = form, composer_id=composer_id)

    c = Composer.query.get(composer_id)
    c.name = form.newname.data
    db.session().commit()

    return redirect(url_for("composers_index"))

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

@app.route("/styles/modify/<style_id>", methods=["GET", "POST"])
@login_required
def styles_modify(style_id):

    if request.method == "GET":
        return render_template("styles/modify.html", form = ModifyForm(), style_id=style_id)

    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("styles/modify.html", form = form, style_id=style_id)

    s = Style.query.get(style_id)
    s.name = form.newname.data
    db.session().commit()

    return redirect(url_for("styles_index"))

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

@app.route("/techniques/modify/<technique_id>", methods=["GET", "POST"])
@login_required
def techniques_modify(technique_id):

    if request.method == "GET":
        return render_template("techniques/modify.html", form = ModifyForm(), technique_id=technique_id)

    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("techniques/modify.html", form = form, technique_id=technique_id)

    t = Technique.query.get(technique_id)
    t.name = form.newname.data
    db.session().commit()

    return redirect(url_for("techniques_index"))
