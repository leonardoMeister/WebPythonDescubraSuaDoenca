from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_acompanhamento = Blueprint('Acompanhamento',__name__, url_prefix="/acompanhamento", template_folder= 'templates')

@bp_acompanhamento.route("/")
@validarSessao
def rotaAcompanhamento():
    return render_template("acompanhamento.html")
