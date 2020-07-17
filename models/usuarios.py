from ..app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuarios(UserMixin, db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_username = db.Column(db.String(100), index=False, unique=False,nullable=False)
    usuario_email = db.Column(db.String(80),index=True,unique=True,nullable=False)
    usuario_senha = db.Column(db.String(200),primary_key=False,unique=False,nullable=False)
