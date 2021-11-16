from datetime import datetime
from flask import Blueprint, render_template , request, send_file, jsonify,session
from funcoes import LogEnum, Funcoes
from dir_login.login import validarSessao
from GeraPdf import PDF
from dao_project.ControlAgendamentos import DAOAgendamentos, Agendamentos
from dao_project.ControlClinica import DAOClinica, Clinica
from dao_project.ModelUsuario import DAOUsuario

bp_agendamento = Blueprint('Agendamento',__name__, url_prefix="/agendamento", template_folder= 'templates')

@bp_agendamento.route("/")
@validarSessao
def rotaAgendamento():
    banco = DAOAgendamentos()
    dados = banco.SelectAll()
    return render_template("agendamento.html", dados = dados)

@bp_agendamento.route("/cadastroAgendamento")
@validarSessao
def rotaCadastroAgendamento():
    agendamento = Agendamentos(dataCriacao="",dataMarcada="",descricao="",suspeita="",tipo="",userId=0,clinicaid=0,idAgendamento=0)
    bancoClinica = DAOClinica()
    clinicas = bancoClinica.SelectAll()
    return render_template("cadastroAgendamento.html", agendamento = agendamento, clinicas = clinicas)

@bp_agendamento.route("/dropAgendamento", methods=['POST'])
@validarSessao
def deletarAgendamento():
    banco = DAOAgendamentos()
    idAgendamento = request.form['id_agendamento']
    banco.Drop(agendamentoId=idAgendamento)
    dados = banco.SelectAll()
    return render_template("agendamento.html", dados = dados)


@bp_agendamento.route("/filtroAgendamento", methods=['POST'])
@validarSessao
def FiltroAgendamento():
    banco = DAOAgendamentos()
    suspeita = request.form['suspeitaAgendamento']
    dados = banco.SelectPorSuspeita( suspeita=suspeita)
    return render_template("agendamento.html", dados = dados)


@bp_agendamento.route("/editAgendamento", methods=['POST'])
@validarSessao
def editarAgendamento():
    idAgendamento = request.form['id_agendamento']
    banco = DAOAgendamentos()
    dados = banco.SelectId(agendamentoId=idAgendamento)
    agendamento = Agendamentos(idAgendamento=dados[0][0], tipo=dados[0][1], dataCriacao=dados[0][2],dataMarcada=dados[0][3], suspeita=dados[0][4], descricao=dados[0][5], userId=dados[0][6], clinicaid=dados[0][7])
    
    new_format = "%Y-%m-%dT%H:%M:%S"
    agendamento.data_marcada = datetime.fromisoformat(agendamento.data_marcada)
    agendamento.data_marcada = agendamento.data_marcada.strftime(new_format)
    print(agendamento.data_marcada)
    print(type(agendamento.data_marcada))
    #2019-11-15T14:30
    bancoClinica = DAOClinica()
    clinicas = bancoClinica.SelectAll()
    return render_template("cadastroAgendamento.html", agendamento = agendamento, clinicas = clinicas)
    
@bp_agendamento.route("/pdfAgendamento")
@validarSessao
def returnPdfAgendamento():
    pdf = PDF()
    #pdf.pdfDoenca()
    Funcoes.criaLog(LogEnum.INFO, LogEnum.load, request.path, session['nome'], "Geração de PDF")
    return send_file("PdfDoencas.pdf", attachment_filename='PdfDoencas.pdf')

@bp_agendamento.route("/validacaoCadastroAgendamento" , methods = ['POST'])
@validarSessao
def validacaoCadastroAgendamento():
    try:
        #Instancia do banco de doenca
        bancoAgendamento = DAOAgendamentos()
        bancoCLinica = DAOClinica()
        bancoUsuario = DAOUsuario()
        #pegando os dados do Formulario web
        nomeClinica = request.form["clinica"]
        dataConsulta = request.form['dataConsulta']
        dataConsulta = datetime.fromisoformat(dataConsulta)
        descricao = request.form['descricao']
        suspeita = request.form['suspeita']
        tipo = request.form['tipo']
        idAgendamento = request.form['id_agendamento']
        nomeUser = session['nome']
        idUsuario = bancoUsuario.SelectEmail(nomeUser).id_usuario
        idClinica = bancoCLinica.selectName(nome=nomeClinica)[0][0]

        #Verificando a existencia de uma doença já com esse nome no banco
        if(dataConsulta == ""):
            #Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Sintomas curto de mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Data Invalida")        
        if (suspeita == "" or len(suspeita)<3):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Suspeita Muito Curta")        
        if (descricao == "" or len(descricao)<15):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Descrição Muito Curta")        
            
    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de campo")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)

    try:        
        if (idAgendamento == 0 or idAgendamento =="0"):
            agendamento = Agendamentos(clinicaid=idClinica,dataMarcada=dataConsulta,descricao=descricao,tipo=tipo,suspeita=suspeita,userId=idUsuario,dataCriacao=datetime.now())
            bancoAgendamento.Insert(agendamento=agendamento)
            return jsonify(erro = False , mensagem = "Adição Banco", mensagem_exception = "Novo Registro Inserido com sucesso")
        else:
            print("PASSOU PELO UPDATE")
            print(tipo)
            print(type(tipo))
            agendamento = Agendamentos( idAgendamento=idAgendamento ,clinicaid=idClinica,dataMarcada=dataConsulta,descricao=descricao,tipo=tipo,suspeita=suspeita,userId=idUsuario,dataCriacao=datetime.now())
            print(agendamento.tipo)
            print(type(agendamento.tipo))
            bancoAgendamento.Update(agendamento=agendamento)
            return jsonify(erro = False , mensagem = "Update Completo", mensagem_exception = "Registro atualizado com sucesso")

    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de campo")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)