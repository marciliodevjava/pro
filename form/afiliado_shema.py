from marshmallow import Schema, fields

from enumerate.message import AfiliadoFormulario


class AfiliadoShema(Schema):
    nome = fields.Str(required=True, error_messages={'required': AfiliadoFormulario.CAMPO_NOME})
    email = fields.Str(required=True, error_messages={'required': AfiliadoFormulario.CAMPO_EMAIL})
    cpf = fields.Str(required=True, error_messages={'required': AfiliadoFormulario.CAMPO_CPF})
    rg = fields.Str(required=True, error_messages={'required': AfiliadoFormulario.CAMPO_PRECO})
