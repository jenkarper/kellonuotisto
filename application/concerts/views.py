from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db
from application.concerts.models import Concert
from application.concerts.forms import ConcertForm

# CONCERT
@app.route("/concerts", methods=["GET"])
def concerts_index():
    concerts = db.session.query(Concert).order_by(Concert.date)
    return render_template("concerts/list.html", concerts = concerts)

@app.route("/concerts/<concert_id>/")
@login_required
def concerts_show(concert_id):
    return render_template("concerts/show.html", concert = Concert.query.get(concert_id))

@app.route("/concerts/new/")
@login_required
def concerts_form():
    return render_template("concerts/new.html", form = ConcertForm())

@app.route("/concerts/", methods=["POST"])
@login_required
def concerts_create():
    form = ConcertForm(request.form)

    if not form.validate():
        return render_template("concerts/new.html", form = form)

    name = form.name.data
    venue = form.venue.data
    date = form.date.data

    c = Concert(name, venue, date)

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("concerts_index"))
