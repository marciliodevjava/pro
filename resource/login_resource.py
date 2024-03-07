from flask import request
from flask_restful import Resource, reqparse

from enumerate.message import UsuarioFormulario, LoginFormulario, MessageLogin
from fomulario.usuario_shema import UsuarioSchema
from service.usuario_service import UsuarioService


class CadastroResource(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=UsuarioFormulario.O_CAMPO_USERNAME)
        self.__parser.add_argument('login', type=str, required=True, help=UsuarioFormulario.O_CAMPO_LOGIN)
        self.__parser.add_argument('senha', type=str, required=True, help=UsuarioFormulario.O_CAMPO_PASSWORD)
        self.__parser.add_argument('email', type=str, required=True, help=UsuarioFormulario.O_CAMPO_EMAIL)

    def post(self):
        # dados = self.__parser.parse_args()
        dados = UsuarioSchema().load(request.json)
        usuario = UsuarioService.cadastro_usuario(dados)
        if usuario.get('message').__eq__(UsuarioFormulario.USUARIO_JA_EXISTE.value):
            return usuario, 200
        if not usuario:
            return {
                'message': UsuarioFormulario.USUARIO_OCORREU_UM_ERRO
            }, 404
        return usuario, 201

    def put(self):
        dados = self.__parser.parse_args()
        usuario = UsuarioService.atualizar_usuario(dados)

    def delete(self):
        dados = self.__parser.parse_args()


class LoginResource(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('login', type=str, required=True, help=LoginFormulario.CAMPO_LOGIN)
        self.__parser.add_argument('senha', type=str, required=True, help=LoginFormulario.CAMPO_SENHA)

    def post(self):
        dados = self.__parser.parse_args()
        usuario = UsuarioService.login_usuario(dados['login'], dados['senha'])
        if usuario.get('token'):
            return usuario, 200
        elif usuario.get('message').__eq__(MessageLogin.LOGIN_SENHA_INCORRETA):
            return usuario, 404
        return usuario, 404
