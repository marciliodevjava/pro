from flask_restful import Resource, reqparse

from enumerate.message import UsuarioFormulario
from service.usuario_service import UsuarioService


class Login(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=UsuarioFormulario.O_CAMPO_USERNAME)
        self.__parser.add_argument('login', type=str, required=True, help=UsuarioFormulario.O_CAMPO_LOGIN)
        self.__parser.add_argument('senha', type=str, required=True, help=UsuarioFormulario.O_CAMPO_PASSWORD)
        self.__parser.add_argument('email', type=str, required=True, help=UsuarioFormulario.O_CAMPO_EMAIL)

    def get(self):
        pass

    def post(self):
        dados = self.__parser.parse_args()
        usuario = UsuarioService.cadastro_ususario(dados)
        if usuario.get('message') == UsuarioFormulario.USUARIO_JA_EXISTE:
            return usuario, 200
        if not usuario:
            return {
                'message': UsuarioFormulario.USUARIO_OCORREU_UM_ERRO
            }
        return usuario, 201

    def put(self):
        pass

    def delete(self):
        pass
