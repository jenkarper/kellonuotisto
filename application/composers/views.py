from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.composers.models import Composer
from application.composers.forms import ComposerForm

@app.route("/composers/", methods=["GET"])
def composers_index():
    return render_template("composers/list.html", composers = Composer.query.all())

@app.route("/composers/new/")
#@login_required
def composers_form():
    return render_template("composers/new.html", form = ComposerForm())

@app.route("/composers/modify/", methods=["GET"])
#@login_required
def composers_modify():
    return redirect(url_for("composers_index"))

@app.route("/composers/", methods=["POST"])
#@login_required
def composers_create():
    form = ComposerForm(request.form)

    if not form.validate():
        return render_template("composers/new.html", form = form)

    c = Composer(form.name.data)

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("composers_index"))
