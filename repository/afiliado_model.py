from config.config import db
from enumerate.message import AfiliadoMessageModel
from utils.formatador_utils import FormatadorDados

class AfiliadoModel(db.Model):
    __tablename__ = 'afiliado'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    rg = db.Column(db.String(15), nullable=False)

    def __init__(self, nome, email, cpf, rg):
        self.nome_completo = nome
        self.email = email
        self.cpf = cpf
        self.rg = rg

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome_completo,
            'email': self.email,
            'cpf': self.cpf,
            'rg': self.rg
        }

    @classmethod
    def salvar(cls, afiliado):
        try:
            buscar = cls.buscar_afiliado_salvar(afiliado)
            if buscar:
                return {
                    'message': AfiliadoMessageModel.AFILIADO_JA_EXISTE.value,
                    'afiliado': buscar.json()
                }
            db.session.add(afiliado)
            db.session.commit()
            return afiliado
        except BaseException as e:
            return None

    @classmethod
    def buscar_afiliado(cls, id):
        try:
            buscar = db.session.query(cls).filter_by(id=id).first()
            if buscar:
                return buscar
            return None
        except BaseException as b:
            return None

    @classmethod
    def buscar_afiliado_salvar(cls, afiliado):
        try:
            buscar = db.session.query(cls).filter_by(nome_completo=afiliado.nome_completo, email=afiliado.email).first()
            if buscar:
                return buscar
            return None
        except BaseException as b:
            return None

    @classmethod
    def atualizar_afiliado(cls, dados, afiliado):
        nome = FormatadorDados.formatador_nome(dados['nome'])
        email = FormatadorDados.formatador_email(dados['email'])
        cpf = FormatadorDados.formatar_cpf(dados['cpf'])
        rg = FormatadorDados.formatar_rg(dados['rg'])
        try:
            afiliado.nome_completo = nome
            afiliado.email = email
            afiliado.cpf = cpf
            afiliado.rg = rg
            db.session.commit()
            return afiliado
        except BaseException as e:
            return None