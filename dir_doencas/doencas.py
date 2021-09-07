from flask import Blueprint, render_template , request

bp_doenca = Blueprint('doenca',__name__, url_prefix="/doença", template_folder= 'templates')

@bp_doenca.route("/")
def rotaMenuDoencas():
    return render_template("doencasMenu.html")

@bp_doenca.route("/dengue")
def rotaDoencaDengue():
    return render_template("doencas.html")