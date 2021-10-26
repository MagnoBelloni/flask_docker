import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        autor = request.form['autor']
        livro = Livros(nome, autor)

        db.session.add(livro)
        db.session.commit()
    
    livros = Livros.query.order_by(Livros.data_criacao.desc()).all()
    return render_template('index.html', livros=livros)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    db.create_all()
    app.run(host='0.0.0.0', port=port)
