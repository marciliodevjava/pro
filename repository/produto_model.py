from config.banco_de_dados import db


class ProdutoModel(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, nome, descricao, quantidade, preco):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    @classmethod
    def buscar_produto(cls, nome, descricao):
        try:
            produto = db.session.query(cls).filter_by(nome=nome, descricao=descricao).first()
            if produto:
                return produto
            return None
        except BaseException as b:
            return None
