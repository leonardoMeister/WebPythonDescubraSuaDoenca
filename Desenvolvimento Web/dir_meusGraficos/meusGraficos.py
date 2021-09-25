from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_meusGraficos = Blueprint('MeusGraficos',__name__, url_prefix="/meusGraficos", template_folder= 'templates')

@bp_meusGraficos.route("/")
@validarSessao
def rotaMeusGraficos():
    return render_template("meusGraficos.html")
