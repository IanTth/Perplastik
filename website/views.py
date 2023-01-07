from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# rotas #

@views.route('/')
def home():
    return render_template("index.html")

@views.route('produtos')
def produtos():
    return render_template('serviços/produtos.html')

@views.route('serviços')
def serviços():
    return render_template('serviços/serviços.html')
    
@views.route('contatos')
def contatos():
    return render_template('contatos.html')

