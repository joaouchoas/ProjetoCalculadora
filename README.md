# Calculadora
Projeto de Conclusão da matéria Laboratório de Engenharia de Software, da FATEC São José dos Campos

## Instruções
- Instalar máquina virtual
<pre>pip install virtualenv</pre>

- Criar máquina virtual
<pre>python -m venv maquina</pre>

- Entrar na máquina virtual
<pre>maquina\Scripts\activate</pre>

- Clonar projeto
<pre>git clone https://github.com/joaouchoas/ProjetoCalculadora.git</pre>
<pre>cd ProjetoCalculadora</pre>

- Instalar as bibliotecas
<pre>pip install -r requirements.txt</pre>

- Executar projeto
<pre>python -m flask run</pre>

## Processo de criação da base de dados
- Configuração do bd
<pre>db_path = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///storage.db"
app.config["SQLALCHEMY_DATABASE_URI"] = db_file</pre>

- Iniciando o SQLAlchemy
<pre>db = SQLAlchemy(app)</pre>

- Usando flask migrate e manager para criação do arquivo
<pre>migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)</pre>

- Criando as tabelas
<pre>db.create_all(app=app)</pre>

## Estrutura do código
<pre>
Controllers
    __init__.py
    calculadora.py
    historico.py
    sessao.py

Models
    __init__.py
    resultados.py
    usuarios.py

Static
    css
        Arquivos de estilos
    img
        Logotipo do app
    js
        Arquivos javascript

Templates
    base.html
    cadastro.html
    calculadora.html
    historico.html
    login.html
</pre>