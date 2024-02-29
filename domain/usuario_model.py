from config.config import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(38), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
