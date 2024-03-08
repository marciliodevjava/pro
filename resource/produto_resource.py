from flask_jwt_extended import jwt_required
from flask_restful import Resource, request
from jwt import ExpiredSignatureError

from enumerate.message import ProdutoMessage
from fomulario.produto_shema import ProdutoShema
from service.produto_service import ProdutoService
from mapper.produto_mapper import ProdutoMapper


class ProdutoResource(Resource):
    @jwt_required()
    def post(self):
        try:
            dados = ProdutoShema().load(request.json)
            produto = ProdutoService.cadastro_produto(dados)
            if produto.get('message').__eq__(ProdutoMessage.PRODUTO_EXISTENTE.value):
                return produto, 200
            if not produto:
                return {
                    'message': ProdutoMessage.PRODUTO_OCORREU_UM_ERRO
                }
            return produto, 201
        except ExpiredSignatureError:
            return {
                'message': 'Token expirado. Faça login novamente para obter um novo token.'
            }, 401
        except Exception as e:
            return {
                'message': f'Ocorreu um erro: {str(e)}'
            }, 500

    def get(self):
        produto = ProdutoService.buscar_todos()
        if produto:
            produto = ProdutoMapper.mapear_produto(produto)
            return {'produto': list(produto)}, 200
        return {
            'message': ProdutoMessage.NAO_EXISTE_PRODUTOS_CADASTRADOS
        }

    def put(self):
        pass

    def delete(self):
        pass
