from flask import Blueprint, render_template , request,jsonify, session, send_file
from dir_login.login import validarSessao
from dao_project.ModelUsuario import DAOUsuario, Usuario 
from GeraPdf import PDF
from funcoes import LogEnum, Funcoes


bp_perfil = Blueprint('Perfil',__name__, url_prefix="/Perfil", template_folder= 'templates')

@bp_perfil.route("/")
@validarSessao
def editarPerfil():
    nome = session['nome']
    banco = DAOUsuario()
    dados = banco.SelectEmail(email=nome)
    Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Carregando dados Perfil")
    return render_template("Perfil.html", dados = dados)







@bp_perfil.route("/pdf")
@validarSessao
def perfilGerarPdf():
    pdf = PDF()
    pdf.pdfPerfil()
    Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Geração de PDF")
    return send_file("PdfDadosPerfil.pdf", attachment_filename='PdfDadosPerfil.pdf')

@bp_perfil.route("/pdfGeral")
@validarSessao
def gerarPdfGeral():
    pdf = PDF()
    pdf.pdfGeral()
    Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Geração de PDF")
    return send_file("DadosGerais.pdf", attachment_filename='DadosGerais.pdf')








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
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Nome Curto de Mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Nome Curto De mais")    
        if(cpf =="" or len(cpf)!= 14):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "CPF Incorreto")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "CPF Curto De Mais")
        if(telefone=="" or len(telefone) < 13):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Telefone incorreto")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Telefone Invalido")

    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de Campo Invalido")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)
    finally:
        pass
    try:
        banco = DAOUsuario()
        usuario = Usuario(nome=nome,cpf=cpf, tipo_sangue=tipoSangue,telefone=telefone,alergia=alergia,email=email)
        banco.Update(user=usuario)
    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.error, request.path, session['nome'], "Erro de banco")
        jsonify(erro = True , mensagem = "ERRO BANCO", mensagem_exception = _msg_exception)

    Funcoes.criaLog(LogEnum.WARNING, LogEnum.save, request.path, session['nome'], "Dados do perfil alterados")
    return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Salvos Com Sucesso, Clique em OK")