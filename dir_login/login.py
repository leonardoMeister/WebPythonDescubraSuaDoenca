from flask import Blueprint, render_template , redirect , request, url_for, session

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
        #LIMPANDO E ADICIONANDO A SESSÃO O USUARIO
        session.clear()
        session['nome'] = nome
        return redirect(url_for("home.rotaHome"))
    else :
        return redirect(url_for('login.login' , falhalogin =1))


@bp_login.route('/logoff' , methods = ['GET'])
def logoff():

    #SERVE PARA LIMPAR UM VALOR INDIVIDUAL
    session.pop('nome' , None)
    #LIMPA TODA A SESSION
    session.clear()

    return redirect(url_for('login.login'))