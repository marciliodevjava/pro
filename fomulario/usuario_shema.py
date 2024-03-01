from marshmallow import Schema, fields

from enumerate.message import UsuarioFormulario


class UsuarioSchema(Schema):
    username = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_USERNAME})
    password = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_PASSWORD})
    email = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_EMAIL})
