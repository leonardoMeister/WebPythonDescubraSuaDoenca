from flask import Blueprint, render_template , request, session, jsonify
from dir_login.login import validarSessao
from dao_project.ControlDoenca import DAODoenca, Doenca
from funcoes import LogEnum, Funcoes

bp_doenca = Blueprint('doenca',__name__, url_prefix="/doença", template_folder= 'templates')

@bp_doenca.route("/")
@validarSessao
def rotaMenuDoencas():
    banco = DAODoenca()
    dados = banco.SelectAll()
    return render_template("pesquisa.html", dados = dados)

@bp_doenca.route("/listagem")
@validarSessao
def listagemDoencas():
    banco = DAODoenca()
    dados = banco.SelectAll()

    return render_template("listaDoencas.html", dados = dados)

@bp_doenca.route("/pesquisa")
@validarSessao
def pesquisaDoencas():
    banco = DAODoenca()
    dados = banco.SelectAll()

    return render_template("pesquisa.html", dados = dados)

@bp_doenca.route("/deleteDoenca", methods=['POST'])
@validarSessao
def deletarDoenca():
    banco = DAODoenca()
    idDoenca = request.form['id_doenca']

    banco.Drop(idDoenca=idDoenca)

    dados = banco.SelectAll()

    return render_template("listaDoencas.html", dados=dados)





@bp_doenca.route("updateDoenca", methods=['POST'])
@validarSessao
def atualizarDoenca():
    banco = DAODoenca()
    idDoenca = request.form['id_doenca']

    dados = banco.SelectId(idDoenca=idDoenca)

    doenca = Doenca(id=dados[0][0],nomeD=dados[0][1],descricaoD=dados[0][2],gravidadeD=dados[0][3],tratamentoD=dados[0][4],sintomasD=dados[0][5])

    return render_template("cadastroDoencas.html", doenca = doenca)

@bp_doenca.route("/cadastrarDoenca")
@validarSessao
def rotaCadastrarNova():
    Funcoes.criaLog(LogEnum.INFO, LogEnum.redirect, request.path, session['nome'], "Redirecionando")
    doenca = Doenca()    
    return render_template("cadastroDoencas.html", doenca = doenca)






@bp_doenca.route("/salvando" , methods = ['POST'])
@validarSessao
def salvandoDoenca():
    try:
        #Instancia do banco de doenca
        banco = DAODoenca()
        #pegando os dados do Formulario web
        nomeDoenca = request.form["nomeDoenca"]
        descricaoDoenca = request.form["descricao"]
        gravidadeDoenca = request.form["gravidade"]
        tratamentoDoenca = request.form["tratamento"]
        sintomasDoenca = request.form["sintomas"]
        idDoenca = request.form['id_doenca']

        #Verificando a existencia de uma doença já com esse nome no banco
        if(len(nomeDoenca)<3):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Nome curto de mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Nome Curto De mais!")        
        if(len(descricaoDoenca)<50):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Descrição curta de mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Descrição precisa de no mínimo 50 caracteres!")        
        if(len(tratamentoDoenca)<50):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Tratamento curto de mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Tratamento precisa de no mínimo 50 caracteres!")        
        if(len(sintomasDoenca)<30):
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Sintomas curto de mais")
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Sintomas precisa de no mínimo 30 caracteres!")        

    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de campo")
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)
    finally:
        pass

    try:
        doenca = Doenca(sintomasD=sintomasDoenca,tratamentoD=tratamentoDoenca,descricaoD=descricaoDoenca,gravidadeD=gravidadeDoenca,nomeD=nomeDoenca)
        dados = banco.SelectPorNome(nomeDoenca)

        if (dados == []  ):
            banco.Insert(doenca=doenca)    
        elif (idDoenca == str( dados[0][0]) ):
            banco.Update(doenca=doenca)
        else:
            return jsonify(erro = True , mensagem = "ERRO BANCO", mensagem_exception = "ERRO DE BANCO")

    except Exception as e:
        _msg_exception = e.args
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.excecao, request.path, session['nome'], "Erro de banco")
        return jsonify(erro = True , mensagem = "ERRO BANCO", mensagem_exception = _msg_exception)
    
    #Deu certo a att no Banco
    Funcoes.criaLog(LogEnum.WARNING, LogEnum.save, request.path, session['nome'], "Dados de doença adicionados no banco")
    return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Salvos Com Sucesso, Clique em OK")