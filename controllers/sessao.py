from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from ..models import Usuarios
from ..app import db
module = Blueprint('sessao', __name__)

#Quando iniciar no /, ele manda pro login
@module.route("/", methods=["GET","POST"])
def main():
    return redirect(url_for('sessao.login'))

#Rota do logoff
@module.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sessao.login'))

#Rota do login
@module.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@module.route("/login", methods=["POST"])
def login_post():
    email = request.form.get('email')
    senha = request.form.get('senha')

    user = Usuarios.query.filter_by(usuario_email=email).first()

    #se o e-mail não estiver no bd, volta login
    if not user:
        return redirect(url_for('sessao.login'))

    #se o hash da senha não conferir, volta login
    elif not check_password_hash(user.usuario_senha,senha):
        return redirect(url_for('sessao.login'))

    #se der certo, loga e vai pra calculadora
    login_user(user)
    return redirect(url_for('calculadora.calculo'))

#Rota do Cadastro
@module.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template('cadastro.html')

@module.route("/cadastro", methods=["POST"])
def cadastro_post():
    username = request.form.get("username")
    email = request.form.get("email")
    senha = request.form.get("senha")

    cadastrar = Usuarios(usuario_username=username, usuario_email=email, usuario_senha=generate_password_hash(senha, method='sha256'))
    db.session.add(cadastrar)
    db.session.commit()

    return redirect(url_for('sessao.login'))
