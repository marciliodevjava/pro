from marshmallow import Schema, fields

from enumerate.message import ProdutoFormulario


class ProdutoShema(Schema):
    nome = fields.Str(required=True, error_messages={'required': ProdutoFormulario.O_CAMPO_NOME})
    descricao = fields.Str(required=True, error_messages={'required': ProdutoFormulario.O_CAMPO_DESCRICAO})
    quantidade = fields.Integer(required=True, error_messages={'required': ProdutoFormulario.O_CAMPO_QUANTIDADE})
    preco = fields.Float(required=True, error_messages={'required': ProdutoFormulario.O_CAMPO_PRECO})
