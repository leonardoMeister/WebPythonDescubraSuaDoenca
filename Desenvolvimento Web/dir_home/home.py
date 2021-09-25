from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/home")
@validarSessao
def rotaHome():
    return render_template("home.html")

@bp_home.route("/usuario")
@validarSessao
def rotaHomeUsuario():
    return render_template("homeUsuario.html")