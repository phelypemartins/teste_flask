from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  dados = {"contato": "221234567", "email": "fms@hotmsail.com"}
  return render_template('contato.html',dados=dados)

  