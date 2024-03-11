from flask_restful import Resource, request

from form.afiliado_shema import AfiliadoShema
from service.afiliado_service import AfiliadoService

class AfiliadoResource(Resource):

    def post(self):
        dados = AfiliadoShema().load(request.json)
        afiliado = AfiliadoService.cadastrar_afiliado(dados)

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
