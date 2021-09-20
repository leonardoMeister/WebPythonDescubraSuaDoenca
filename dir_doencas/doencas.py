from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_doenca = Blueprint('doenca',__name__, url_prefix="/doença", template_folder= 'templates')

@bp_doenca.route("/")
@validarSessao
def rotaMenuDoencas():
    return render_template("doencasMenu.html")

@bp_doenca.route("/dengue")
@validarSessao
def rotaDoencaDengue():
    return render_template("doencas.html")