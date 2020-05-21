from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.styles.models import Style
from application.styles.forms import StyleForm

@app.route("/styles", methods=["GET"])
def styles_index():
    return render_template("styles/list.html", styles = Style.query.all())

@app.route("/styles/new/")
#@login_required
def styles_form():
    return render_template("styles/new.html", form = StyleForm())

@app.route("/styles/", methods=["POST"])
#@login_required
def styles_create():
    form = StyleForm(request.form)

    if not form.validate():
        return render_template("styles/new.html", form = form)

    s = Style(form.name.data)

    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("styles_index"))
