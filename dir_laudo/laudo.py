from flask import Blueprint, render_template , request

bp_laudo = Blueprint('Laudo',__name__, url_prefix="/laudo", template_folder= 'templates')

@bp_laudo.route("/")
def rotaLaudo():
    return render_template("laudo.html")
