from application import app, db
from flask import render_template, request
from application.composers.models import Composer

@app.route("/composers/new/")
def composers_form():
    return render_template("composers/new.html")

@app.route("/composers/", methods=["POST"])
def composers_create():
    c = Composer(request.form.get("name"))

    db.session().add(c)
    db.session().commit()
  
    return "If music be the food of love, sing on!"
