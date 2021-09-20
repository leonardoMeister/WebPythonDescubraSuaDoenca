from types import MethodType
from flask import Blueprint, render_template , redirect , request, url_for

bp_login = Blueprint('login',__name__, url_prefix="/", template_folder= 'templates')

@bp_login.route("/", methods = ['POST' , 'GET'] )
def login():
    return render_template("login.html" , falhalogin = 0)

@bp_login.route("/login", methods = ['POST'])
def validarLogin():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']

    if (nome == "admin" and senha == "admin"):
        return redirect(url_for("home.rotaHome"))
    else :
        return redirect(url_for('login.login' , falhalogin =1))


@bp_login.route('/logoff' , methods = ['GET'])
def validarLogoff():
    return redirect(url_for('login.login'))