from flask_jwt_extended import create_access_token

from enumerate.message import UsuarioFormulario, MessageLogin
from repository.usuario_model import UsuarioModel
from utils.encriptador_de_senha import gerador_password_hash, check_password_hash


class UsuarioService:
    @classmethod
    def cadastro_usuario(cls, dados):
        login = UsuarioModel.buscar(dados['login'])
        if login:
            return {
                'message': UsuarioFormulario.USUARIO_JA_EXISTE.value
            }
        nome = dados['nome']
        login = dados['login']
        senha = gerador_password_hash(dados['senha'])
        email = dados['email']

        usuario = UsuarioModel(nome=nome, login=login, senha=senha, email=email)
        try:
            usuario = UsuarioModel.salvar(usuario)
            if usuario:
                return {
                    'message': UsuarioFormulario.USUARIO_CRIADO.value,
                    'usuario': usuario.json()
                }
        except Exception as e:
            return None

    @classmethod
    def login_usuario(cls, login, senha):
        usuario = UsuarioModel.buscar(login)
        if usuario:
            if usuario and check_password_hash(senha, usuario.senha):
                access_token = create_access_token(identity=usuario.id)
                return {
                    'message': MessageLogin.LOGIN_EFETUADO_COM_SUCESSO.value,
                    'token': access_token,
                    'nome': usuario.nome,
                    'login': login
                }
            else:
                return {
                    'message': MessageLogin.LOGIN_SENHA_INCORRETA.value,
                    "login": login
                }
        return {
            'message': MessageLogin.USUARIO_NAO_EXISTE.value
        }
