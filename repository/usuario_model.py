from config.banco_de_dados import db


class UsuarioModel(db.Model):
    __tablename__: 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email
