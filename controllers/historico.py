from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from ..models import Resultados
from ..app import db
module = Blueprint("historico", __name__)


@module.route("/historico", methods=["GET"])
@login_required
def historico():
    historico = Resultados.query.all()
    #usar o ::-1 para aparecer do mais recente para o mais antigo, caso contrário, sempre aparece primeiro as
    #primeiras inserções
    historico = historico[::-1]
    return render_template('historico.html', historico = historico)
        