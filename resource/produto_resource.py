from flask_restful import Resource, request

from enumerate.message import ProdutoMessage
from fomulario.produto_shema import ProdutoShema
from service.produto_service import ProdutoService


class ProdutoResource(Resource):
    def post(self):
        dados = ProdutoShema.load(request.json)
        produto = ProdutoService.cadastro_produto(dados)
        if produto.get('message').__eq__(ProdutoMessage.PRODUTO_EXISTENTE.value):
            return produto, 200
        if not produto:
            return {
                'message': ProdutoMessage.PRODUTO_OCORREU_UM_ERRO
            }
        return produto, 201

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass