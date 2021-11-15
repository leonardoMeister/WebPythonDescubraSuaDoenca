from flask import Blueprint, render_template , request
from dir_login.login import validarSessao
from dao_project.ControlAgendamentos import DAOAgendamentos, Agendamentos
bp_agendamento = Blueprint('Agendamento',__name__, url_prefix="/agendamento", template_folder= 'templates')

@bp_agendamento.route("/")
@validarSessao
def rotaAgendamento():
    banco = DAOAgendamentos()
    dados = banco.SelectAll()
    return render_template("agendamento.html", dados = dados)
