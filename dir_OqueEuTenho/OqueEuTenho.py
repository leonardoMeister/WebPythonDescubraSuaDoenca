from flask import Blueprint, render_template , request

bp_OqueEuTenho = Blueprint('OqueEuTenho',__name__, url_prefix="/OqueEuTenho", template_folder= 'templates')

@bp_OqueEuTenho.route("/")
def rotaOqueEuTenho():
    return render_template("OqueEuTenho.html")
