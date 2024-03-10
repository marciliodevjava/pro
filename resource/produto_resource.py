from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from enumerate.message import ProdutoMessage
from form.produto_shema import ProdutoShema
from mapper.produto_mapper import ProdutoMapper
from service.produto_service import ProdutoService


class ProdutoResource(Resource):
    @jwt_required()
    def post(self):
        dados = ProdutoShema().load(request.json)
        produto = ProdutoService.cadastro_produto(dados)
        if produto.get('message').__eq__(ProdutoMessage.PRODUTO_EXISTENTE.value):
            return produto, 200
        if not produto:
            return {
                'message': ProdutoMessage.PRODUTO_OCORREU_UM_ERRO
            }, 500
        return produto, 201

    def get(self):
        produto = ProdutoService.buscar_todos()
        if produto:
            produto = ProdutoMapper.mapear_produto(produto)
            return {'produto': list(produto)}, 200
        return {
            'message': ProdutoMessage.NAO_EXISTE_PRODUTOS_CADASTRADOS
        }

    def put(self, id):
        dados = ProdutoShema().load(request.json)
        produto = ProdutoService.atualizar_produto(dados, id)
        if produto.get('message').__eq__(ProdutoMessage.NAO_EXISTE_ESSE_PRODUTO_PARA_ATUALIZAR.value):
            return {
                'message': ProdutoMessage.NAO_EXISTE_ESSE_PRODUTO_PARA_ATUALIZAR
            }, 404
        if not produto:
            return {
                'message': ProdutoMessage.OCORREU_UM_ERRO_AO_ATUALIZAR_PRODUTO
            }, 500
        return produto, 201

    def delete(self, id):
        produto = ProdutoService.deletar_produto(id)
        if produto.get('message').__eq__(ProdutoMessage.OCORREU_UM_ERRO_AO_DELETAR_PRODUTO.value):
            return produto, 500
        return produto, 200
