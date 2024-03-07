from marshmallow import Schema, fields

from enumerate.message import UsuarioFormulario


class UsuarioSchema(Schema):
    nome = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_USERNAME})
    login = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_LOGIN})
    senha = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_PASSWORD})
    email = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_EMAIL})
