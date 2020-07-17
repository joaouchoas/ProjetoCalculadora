from ..app import db
from . import Usuarios

class Resultados(db.Model):
    __tablename__ = 'resultados'

    id_resultado = db.Column(db.Integer, primary_key=True)
    conta_resultado = db.Column(db.String(100), index=False, unique=False,nullable=False)
    horario_resultado = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    usuario_resultado = db.Column(db.String(100), index=False, unique=False,nullable=False)
