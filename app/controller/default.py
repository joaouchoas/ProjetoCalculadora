from app import app
from app import render_template

@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/index", methods=["GET"])
def login():
    return render_template("index.html")

@app.route("/historico", methods=["GET"])
def historico():
    return render_template("historico.html")