from enumerate.message import UsuarioFormulario
from repository.usuario_model import UsuarioModel
from utils.encriptador_de_senha import gerador_password_hash


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
