from flask import Blueprint, render_template , request, session
from dir_login.login import validarSessao
from funcoes import Funcoes, LogEnum

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/home")
@validarSessao
def rotaHome():
    Funcoes.criaLog(LogEnum.INFO, LogEnum.redirect, request.path, session['nome'], "Home Acessada")
    return render_template("home.html")
