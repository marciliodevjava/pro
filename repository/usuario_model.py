from config.banco_de_dados import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, login, senha, email):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email

    def json(self):
        return {
            'nome': self.nome,
            'login': self.login,
            'email': self.email
        }

    def __eq__(self, dados):
        if (dados):
            return (
                    self.nome == dados['nome'] and
                    self.login == dados['login'] and
                    self.email == dados['email']
            )
        return False
    @classmethod
    def buscar(cls, login):
        try:
            login = db.session.query(cls).filter_by(login=login).first()
            if login:
                return login
            return None
        except BaseException as b:
            return None

    @classmethod
    def salvar(cls, usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except BaseException as b:
            return None

    @classmethod
    def atualizar(cls, nome, email, usuario):
        try:
            if usuario:
                usuario.nome = nome
                usuario.email = email
                db.session.commit()
                return usuario
            return None
        except BaseException as e:
            return None
