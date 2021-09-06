from flask import Blueprint, render_template , request

bp_meusGraficos = Blueprint('MeusGraficos',__name__, url_prefix="/meusGraficos", template_folder= 'templates')

@bp_meusGraficos.route("/")
def rotaMeusGraficos():
    return render_template("meusGraficos.html")
