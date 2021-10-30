from re import S
from flask import Blueprint, render_template , request, session, jsonify
from dir_login.login import validarSessao
from dao_project.ControlDoenca import DAODoenca, Doenca

bp_doenca = Blueprint('doenca',__name__, url_prefix="/doença", template_folder= 'templates')

@bp_doenca.route("/")
@validarSessao
def rotaMenuDoencas():
    return render_template("doencas.html")

@bp_doenca.route("/cadastrarDoenca")
@validarSessao
def rotaCadastrarNova():
    return render_template("cadastroDoencas.html")


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

        #Verificando a existencia de uma doença já com esse nome no banco
        if (banco.SelectName(nomeDoenca) != []  ):
            return jsonify(erro = True , mensagem = "Doença Inválida", mensagem_exception = "Essa doença já está cadastrada!")        
        if(len(nomeDoenca)<3):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Nome Curto De mais!")        
        if(len(descricaoDoenca)<50):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Descrição precisa de no mínimo 50 caracteres!")        
        if(len(tratamentoDoenca)<50):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Tratamento precisa de no mínimo 50 caracteres!")        
        if(len(sintomasDoenca)<30):
            return jsonify(erro = True , mensagem = "Erro de Campo", mensagem_exception = "Sintomas precisa de no mínimo 30 caracteres!")        

    except Exception as e:
        _msg_exception = e.args
        return jsonify(erro = True , mensagem = "Campo Invalido", mensagem_exception = _msg_exception)
    finally:
        pass


    try:
        doenca = Doenca(sintomasD=sintomasDoenca,tratamentoD=tratamentoDoenca,descricaoD=descricaoDoenca,gravidadeD=gravidadeDoenca,nomeD=nomeDoenca)
        banco.Insert(doenca=doenca)

    except Exception as e:
        _msg_exception = e.args
        jsonify(erro = True , mensagem = "ERRO BANCO", mensagem_exception = _msg_exception)
    
    #Deu certo a att no Banco
    return jsonify(erro = False , mensagem = "Sucesso", mensagem_exception = "Dados Salvos Com Sucesso, Clique em OK")