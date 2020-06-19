from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.concerts.models import Concert
from application.concerts.forms import ConcertForm, EditForm
from application.supplements.forms import DeleteForm

@app.route("/concerts", methods=["GET"])
@login_required
def concerts_index():
    concerts = Concert.list_concerts()
    return render_template("concerts/list.html", concerts = concerts)

@app.route("/concerts/<concert_id>/")
@login_required
def concerts_show(concert_id):
    concert = Concert.query.get(concert_id)
    pieces = concert.pieces
    return render_template("concerts/show.html", concert = concert, pieces = pieces)

@app.route("/concerts/new/")
@login_required(role="ADMIN")
def concerts_form():
    return render_template("concerts/new.html", form = ConcertForm())

@app.route("/concerts/", methods=["POST"])
@login_required(role="ADMIN")
def concerts_create():
    form = ConcertForm(request.form)

    if not form.validate():
        return render_template("concerts/new.html", form = form)

    name = request.form["name"]
    venue = request.form["venue"]
    date = request.form["date"]

    concert = Concert(name, venue, date)

    db.session().add(concert)
    db.session().commit()
  
    return redirect(url_for("concerts_index"))

@app.route("/concerts/delete/<concert_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def concerts_delete(concert_id):
    concert = Concert.query.get(concert_id)

    if request.method == "GET":
        return render_template("concerts/delete.html", form = DeleteForm(), concert_id = concert_id, concert = concert)

    form = DeleteForm(request.form)

    c = Concert.query.get(concert_id)

    if c.pieces:
        return "This concert is referred to in another table and cannot be deleted!"
    
    db.session().delete(c)
    db.session().commit()

    return render_template("success.html")

@app.route("/concerts/edit/<concert_id>", methods = ["GET", "POST"])
@login_required
def concerts_edit(concert_id):
    concert = Concert.query.get(concert_id)

    if request.method == "GET":
        return render_template("concerts/edit.html", form = EditForm(), concert = concert, concert_id = concert_id)

    form = EditForm(request.form)
    newname = request.form["newname"]
    newvenue = request.form["newvenue"]
    newdate = request.form["newdate"]

    concert.name = newname
    concert.venue = newvenue
    concert.date = newdate

    db.session().commit()

    return redirect(url_for("concerts_show", concert_id=concert_id))
