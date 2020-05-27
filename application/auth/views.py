from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

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
  
    return "User created successfully!"

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password_hash=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjätunnusta tai salasanaa ei löydy.")


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
