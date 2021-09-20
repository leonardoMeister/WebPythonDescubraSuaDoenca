from flask import Blueprint, render_template , request

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/home")
def rotaHome():
    return render_template("home.html")

@bp_home.route("/usuario")
def rotaHomeUsuario():
    return render_template("homeUsuario.html")