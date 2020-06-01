from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from application import app, db
from application.auth.models import User, Note
from application.auth.forms import LoginForm, PasswordForm, RegistrationForm, NoteForm
from application.pieces.models import Piece

# USER
@app.route("/auth/register/")
def auth_form():
    return render_template("auth/register.html", form = RegistrationForm())

@app.route("/auth/", methods = ["POST"])
def auth_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form)

    name = form.name.data
    username = form.username.data
    password = form.password.data
    admin = form.admin.data

    u = User(name, username, password, admin)

    db.session().add(u)
    db.session().commit()
  
    return render_template("success.html")

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=request.form["username"], password_hash=request.form["user_password"]).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Käyttäjätunnusta tai salasanaa ei löydy.")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/list", methods = ["GET"])
@login_required
def auth_index():
    return render_template("auth/list.html", users = User.query.all())

@app.route("/auth/<user_id>", methods = ["GET", "POST"])
def auth_profile(user_id):

    if request.method == "GET":
        return render_template("auth/profile.html", user = current_user, form = PasswordForm())

    form = PasswordForm(request.form)

    if not form.validate():
        return render_template("auth/profile.html", user = current_user, form = form)

    newpassword = request.form["newpassword"]
    u = User.query.get(current_user.id)
    u.password_hash = newpassword

    db.session().commit()

    return render_template("success.html")

#NOTE
@app.route("/notes", methods=["GET"])
def notes_index():
    notes = Note.query.filter_by(user_id=current_user.id)
    return render_template("notes/list.html", notes = notes, user = current_user)

@app.route("/pieces/notes/<piece_id>", methods=["GET", "POST"])
@login_required
def notes_create(piece_id):
    piece = Piece.query.get(piece_id)

    if request.method == "GET":
        return render_template("notes/new.html", form = NoteForm(), piece = piece, piece_id = piece_id)

    form = NoteForm(request.form)

    comment = request.form.get("comment")
    user_id = current_user.id
    piece_id = piece_id
    piece_name = Piece.query.get(piece_id).name

    n = Note(comment, user_id, piece_id, piece_name)
    
    db.session().add(n)
    db.session().commit()

    return redirect(url_for("pieces_show", piece_id=piece_id))
