from app import app
from flask import render_template
from flask import request
from aplicacao import minha_aplicacao

@app.route('/')
@app.route('/index')

def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  dados = {"contato": "221234567", "email": "fms@hotmsail.com"}
  return render_template('contato.html',dados=dados)

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
  usuario = request.args.get('usuario')
  senha = request.args.get('senha')
  return "usuário {} senha {}" .format(usuario, senha)

@app.route('/aplicativo')
def aplicativo():
  resultado = minha_aplicacao()
  return render_template('/aplicativo.html', resultado=resultado)

  