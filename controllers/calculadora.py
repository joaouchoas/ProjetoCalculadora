from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from ..models import Resultados
from ..app import db
module = Blueprint("calculadora", __name__)


@module.route("/calculadora", methods=["GET"])
@login_required
def calculo():
    return render_template('calculadora.html')

@module.route("/calculadora", methods=["POST"])
@login_required
def calculo_post():
    A = request.form.get("A")
    operador = request.form.get("operador")
    B = request.form.get("B")
    resultado = calcular(A,operador,B)

    #Fazer o insert dos dados no bd
    inserir_resultado_bd = Resultados(conta_resultado=resultado, horario_resultado = datetime.now(), usuario_resultado=current_user.usuario_username)
    db.session.add(inserir_resultado_bd)
    db.session.commit()
    return render_template('calculadora.html', resultado = resultado)

#lembrar que todos os números na verdade são strings para fazer a lógica
def calcular(A,operacao_form,B):
    if operacao_form == "adicao":
        conta = str(A) + " + " + str(B) + " = " + str(float(A) + float(B))
    if operacao_form == "subtracao":
        conta = str(A) + " - " + str(B) + " = " + str(float(A)-float(B))
    if operacao_form == "multiplicacao":
        conta = str(A) + " * " + str(B) + " = " + str(float(A)*float(B))
    if operacao_form == "divisao":
        if B == str('0'):
            conta = 'Você feriu o 11º mandamento da Matemática: Divisão por zero NÃO EXISTE!'
        else:
            conta = str(A) + " / " + str(B) + " = " + str(float(A)/float(B))
    if operacao_form == "potenciacao":
            conta = str(A) + " ** "+ str(B) + " = " + str(float(A)**float(B))
    if operacao_form == "radiciacao":
        #Lembrar sempre que a radiciação é uma potenciaçaõ com o segundo número inverso na fração
            conta = str(A) + " √ "+ str(B) + " = " + str(float(A)**(1/float(B)))
    return conta
