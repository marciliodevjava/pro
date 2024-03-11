from config.config import db


class AfiliadoModel(db.Model):
    __tablename__ = 'afiliado'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    rg = db.Column9(db.String(15), nullable=False)

    def __init__(self, nome, email, cpf, rg):
        self.nome_completo = nome
        self.email = email
        self.cpf = cpf
        self.rg = rg

    @classmethod
    def salvar(cls, afiliado):
        try:
            db.session.add(afiliado)
            db.session.commit()
            return afiliado
        except BaseException as e:
            return None