from flask_restful import Resource, request
from fomulario.produto_shema import ProdutoShema
from service.produto_service import ProdutoService

class ProdutoResource(Resource):
    def post(self):
        dados = ProdutoShema.load(request.json)
        produto = ProdutoService.cadastro_produto(dados)

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
