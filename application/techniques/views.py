from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.techniques.models import Technique
from application.techniques.forms import TechniqueForm

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
