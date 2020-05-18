from application import app, db
from flask import redirect, render_template, request, url_for
from application.composers.models import Composer

@app.route("/composers/", methods=["GET"])
def composers_index():
    return render_template("composers/list.html", composers = Composer.query.all())

@app.route("/composers/new/")
def composers_form():
    return render_template("composers/new.html")

@app.route("/composers/modify/", methods=["GET"])
def composers_modify():
    return redirect(url_for("composers_index"))

@app.route("/composers/", methods=["POST"])
def composers_create():
    c = Composer(request.form.get("name"))

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("composers_index"))
