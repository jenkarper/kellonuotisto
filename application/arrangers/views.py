from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.arrangers.models import Arranger
from application.arrangers.forms import ArrangerForm

@app.route("/arrangers", methods=["GET"])
def arrangers_index():
    return render_template("arrangers/list.html", arrangers = Arranger.query.all())

@app.route("/arrangers/new/")
#@login_required
def arrangers_form():
    return render_template("arrangers/new.html", form = ArrangerForm())

@app.route("/arrangers/", methods=["POST"])
#@login_required
def arrangers_create():
    form = ArrangerForm(request.form)

    if not form.validate():
        return render_template("arrangers/new.html", form = form)
    
    a = Arranger(form.name.data)

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("arrangers_index"))



