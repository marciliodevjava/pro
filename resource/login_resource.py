from flask_restful import Resource, reqparse

from enumerate.message import UsuarioFormulario


class Login(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=UsuarioFormulario.O_CAMPO_USERNAME)
        self.__parser.add_argument('senha', type=str, required=True, help=UsuarioFormulario.O_CAMPO_PASSWORD)
        self.__parser.add_argument('email', type=str, required=True, help=UsuarioFormulario.O_CAMPO_EMAIL)

    def get(self):
        pass

    def post(self):
        pass

    def cadastro(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
