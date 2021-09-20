from flask import Blueprint, render_template , request
from dir_login.login import validarSessao

bp_agendamento = Blueprint('Agendamento',__name__, url_prefix="/agendamento", template_folder= 'templates')

@bp_agendamento.route("/")
@validarSessao
def rotaAgendamento():
    return render_template("agendamento.html")
