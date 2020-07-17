import os

#importar o Flask
from flask import Flask

#SQLAlchemy usa o SQL no FLask
from flask_sqlalchemy import SQLAlchemy

#FlaskLogin controla a sessão do usuário no app
from flask_login import LoginManager

#Flassk script e migrate
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#A variável app vai fazer todo o controle do Flask dentro da aplicação
app = Flask(__name__)


#CONFIGURAÇÕES DO ARQUIVO

#BD - Usar o path pra dar certo, definir o arquivo, puxar o arquivo pro Alchemy, colocar a chave secreta
db_path = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///storage.db"
app.config["SQLALCHEMY_DATABASE_URI"] = db_file
#secret key gerada no google cloud
app.config['SECRET_KEY'] = 'iJ1G9CkJr3MVasozKJew5MqqnF9LhWUe'
#definir essa variável para interromper o warning que fica aparecendo na execução no cmd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ---------- FIM CONFIG ----------

#Iniciar a variável db, que vai controlar todo o banco de dados do flask (varivavel app)
db = SQLAlchemy(app)

#usando o flask migrate e o manager para criar o arquivo do bd
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#Login, abrir a instancia, depois puxar o controller e por fim iniciar
login_manager = LoginManager()
login_manager.login_view = 'sessao.login'
login_manager.init_app(app)

#Executar os bancos de dados da aplicação, no caso usuário e resultados
from .models import Usuarios
from .models import Resultados

#Comando pra criar o arquivo .db das tabelas
db.create_all(app=app)

#Fazer login, query no Bd de usuário
@login_manager.user_loader
def load_user(id_usuario):
    return Usuarios.query.get(int(id_usuario))

#Fazer as declarações blueprint, para tornar o código mais modular
from .controllers import sessao as bp_sessao
app.register_blueprint(bp_sessao)

from .controllers import calculadora as bp_calculadora
app.register_blueprint(bp_calculadora)

from .controllers import historico as bp_historico
app.register_blueprint(bp_historico)

#Rodar o arquivo
if __name__ == '__main__':
    app.run(debug=True)
    