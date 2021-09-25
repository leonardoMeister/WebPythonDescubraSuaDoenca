from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_OqueEuTenho = Blueprint('OqueEuTenho',__name__, url_prefix="/OqueEuTenho", template_folder= 'templates')

@bp_OqueEuTenho.route("/")
@validarSessao
def rotaOqueEuTenho():
    return render_template("OqueEuTenho.html")
