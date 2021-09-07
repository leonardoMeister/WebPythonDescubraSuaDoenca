from flask import Blueprint, render_template , request

bp_acompanhamento = Blueprint('Acompanhamento',__name__, url_prefix="/acompanhamento", template_folder= 'templates')

@bp_acompanhamento.route("/")
def rotaAcompanhamento():
    return render_template("acompanhamento.html")
