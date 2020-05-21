from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

@app.route("/auth/register/")
def auth_form():
    return render_template("auth/register.html", form = RegistrationForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form)

    name = form.name.data
    username = form.username.data
    password = form.password.data

    u = User(name, username, password)

    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("auth_login"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password_hash=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    
