import datetime
from app import db

class Livros(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.data_criacao = datetime.datetime.now()
