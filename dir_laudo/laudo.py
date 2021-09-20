from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_laudo = Blueprint('Laudo',__name__, url_prefix="/laudo", template_folder= 'templates')

@bp_laudo.route("/")
@validarSessao
def rotaLaudo():
    return render_template("laudo.html")
