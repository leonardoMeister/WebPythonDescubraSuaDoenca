from flask import Blueprint, render_template , request,jsonify, session, send_file
from dir_login.login import validarSessao
from dao_project.ControlEndereco import DAOEndereco, Endereco
from dao_project.ModelUsuario import DAOUsuario, Usuario
from GeraPdf import PDF
from funcoes import LogEnum, Funcoes


bp_endereco = Blueprint('Endereco',__name__, url_prefix="/Endereco", template_folder= 'templates')


@bp_endereco.route("/")
@validarSessao
def editarEndereco():
    email = session['nome']
    bancoEndereco = DAOEndereco()
    bancoUser = DAOUsuario()
    dadosUser = bancoUser.SelectEmail(email=email)
    
    if dadosUser.endereco:
        Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Carregando dados Endereco")
        dadosEndereco= bancoEndereco.SelectId(id_endereco=dadosUser.endereco)
        return render_template("Endereco.html", dados = dadosEndereco)    
    else:
        Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Carregando dados Endereco Sem sucesso")
        dadosEndereco = Endereco(cidade="",estado="",id_endereco="0",numero="",rua="")
        return render_template("Endereco.html", dados = dadosEndereco)






@bp_endereco.route("/geraPdf")
@validarSessao
def enderecoGerarPdf():
    pdf = PDF()
    pdf.pdfEndereco()
    Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Geração de PDF")
    return send_file("PdfDadosEndereco.pdf", attachment_filename='PdfDadosEndereco.pdf')







@bp_endereco.route("/salvo" , methods = ['POST'])
@validarSessao
def salvandoDados():

    try:
        numero = request.form['Numero']
        rua = request.form['Rua']
        estado = request.form['Estado']
        cidade = request.form['cidade']
        email = session['nome']

        #verificação de campos
        ###############
        ##################
    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de Campo Invalido")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)

    try:
        bancoEndereco = DAOEndereco()
        bancoUser = DAOUsuario()
        dadosUser = bancoUser.SelectEmail(email=email)

        if dadosUser.endereco:
            Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Carregando dados Endereco")
            idEndereco= dadosUser.endereco
            endereco = Endereco(cidade=cidade,estado=estado,id_endereco=idEndereco,numero=numero,rua=rua)
            bancoEndereco.Update(endereco=endereco)
            return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Atualizados com Sucesso!")
        else:
            Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Carregando dados Endereco Sem sucesso")
            endereco = Endereco(cidade=cidade,estado=estado,numero=numero,rua=rua)
            bancoEndereco.Insert(endereco=endereco)
            idEnderecoNovo = bancoEndereco.LastInsert()
            dadosUser.endereco = idEnderecoNovo[0][0]
            bancoUser.UpdateEndereco(dadosUser)
            return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Inseridos com Sucesso!")
        
    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de Campo Invalido")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)
    
