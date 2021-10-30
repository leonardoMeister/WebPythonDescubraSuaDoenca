from flask import Blueprint, render_template , request,jsonify, session
from dir_login.login import validarSessao
from dao_project.ModelUsuario import DAOUsuario, Usuario 



bp_perfil = Blueprint('Perfil',__name__, url_prefix="/Perfil", template_folder= 'templates')

@bp_perfil.route("/")
@validarSessao
def editarPerfil():
    nome = session['nome']
    banco = DAOUsuario()
    dados = banco.SelectEmail(email=nome)
    return render_template("Perfil.html", dados = dados)

@bp_perfil.route("/salvo" , methods = ['POST'])
@validarSessao
def salvandoDados():
    try:
        nome = request.form['nome']
        cpf = request.form['cpf']
        tipoSangue = request.form['tipoSangue']
        telefone = request.form['telefone']
        telefone = telefone.replace(" ","")
        alergia = request.form['alergia']
        email = session['nome']

        if(nome =="" or len(nome)<4 ):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Nome Curto De mais")    
        if(cpf =="" or len(cpf)!= 14):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "CPF Curto De Mais")
        if(telefone=="" or len(telefone) < 13):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Telefone Invalido")

    except Exception as e:
        _msg_exception = e.args
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)
    finally:
        pass
    try:
        banco = DAOUsuario()
        usuario = Usuario(nome=nome,cpf=cpf, tipo_sangue=tipoSangue,telefone=telefone,alergia=alergia,email=email)
        banco.Update(user=usuario)
    except Exception as e:
        _msg_exception = e.args
        jsonify(erro = True , mensagem = "ERRO BANCO", mensagem_exception = _msg_exception)
    return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Salvos Com Sucesso, Clique em OK")