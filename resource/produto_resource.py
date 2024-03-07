from flask_restful import Resource, request
from fomulario.produto_shema import ProdutoShema


class ProdutoResource(Resource):
    def post(self):
        dados = ProdutoShema.load(request.json)

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
