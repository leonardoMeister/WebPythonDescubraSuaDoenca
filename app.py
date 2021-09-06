from flask import Flask , render_template, url_for 
from dir_home.home import bp_home
from dir_doencas.doencas import bp_doenca

app = Flask(__name__) 

app.register_blueprint(bp_home)
app.register_blueprint(bp_doenca)


@app.errorhandler(404)
def rotaErro404(error):
    return render_template("form_404.html"), 404


if __name__ == "__main__":
    app.run(debug= True, port= 5000)