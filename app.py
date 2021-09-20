from flask import Flask , render_template, url_for , redirect, request
from dir_home.home import bp_home
from dir_doencas.doencas import bp_doenca
from dir_OqueEuTenho.OqueEuTenho import bp_OqueEuTenho
from dir_acompanhamento.acompanhamento import bp_acompanhamento
from dir_agendamento.agendamento import bp_agendamento
from dir_meusGraficos.meusGraficos import bp_meusGraficos
from dir_laudo.laudo import bp_laudo
from dir_login.login import bp_login

app = Flask(__name__) 

app.register_blueprint(bp_login)
app.register_blueprint(bp_laudo)
app.register_blueprint(bp_meusGraficos)
app.register_blueprint(bp_agendamento)
app.register_blueprint(bp_home)
app.register_blueprint(bp_doenca)
app.register_blueprint(bp_OqueEuTenho)
app.register_blueprint(bp_acompanhamento)

@app.errorhandler(404)
def rotaErro404(error):
    return render_template("form_404.html"), 404


if __name__ == "__main__":
    app.run(debug= True, port= 5000)