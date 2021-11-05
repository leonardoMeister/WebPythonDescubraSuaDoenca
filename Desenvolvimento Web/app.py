from flask import Flask , render_template,  session, request
from datetime import timedelta
import os

from dir_home.home import bp_home
from dir_doencas.doencas import bp_doenca
from dir_perfil.Perfil import bp_perfil
from dir_acompanhamento.acompanhamento import bp_acompanhamento
from dir_agendamento.agendamento import bp_agendamento
from dir_meusGraficos.meusGraficos import bp_meusGraficos
from dir_laudo.laudo import bp_laudo
from dir_login.login import bp_login
from dir_endereco.Endereco import bp_endereco

app = Flask(__name__) 

app.secret_key = os.urandom(12).hex()

app.register_blueprint(bp_login)
app.register_blueprint(bp_laudo)
app.register_blueprint(bp_meusGraficos)
app.register_blueprint(bp_agendamento)
app.register_blueprint(bp_home)
app.register_blueprint(bp_doenca)
app.register_blueprint(bp_perfil)
app.register_blueprint(bp_acompanhamento)
app.register_blueprint(bp_endereco)


@app.errorhandler(404)
def rotaErro404(error):
    return render_template("form_404.html"), 404

#FUNÇÃO PARA DEFINIR O TEMPO MAXIMO DA SESSAO, SE ESTA ATIVA OU NÃO PELO TEMPO
@app.before_request
def before_request():
    session.permanent = True
    tempo = 6
    #SERVE PARA TER UMA FORMA DE ACESSAR O VALOR TEMPO EM OUTROS LUGARES DA SESSAO
    session['tempo'] = tempo
    app.permanent_session_lifetime = timedelta(minutes = tempo)
    
if __name__ == "__main__":
    app.run(debug= True, port= 5000)
