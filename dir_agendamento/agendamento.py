from flask import Blueprint, render_template , request

bp_agendamento = Blueprint('Agendamento',__name__, url_prefix="/agendamento", template_folder= 'templates')

@bp_agendamento.route("/")
def rotaAgendamento():
    return render_template("agendamento.html")
