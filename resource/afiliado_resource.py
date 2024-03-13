from flask_restful import Resource, request

from enumerate.message import AfiliadoMessageModel, AfiliadoMessage
from form.afiliado_shema import AfiliadoShema
from service.afiliado_service import AfiliadoService


class AfiliadoResource(Resource):

    def post(self):
        dados = AfiliadoShema().load(request.json)
        afiliado = AfiliadoService.cadastrar_afiliado(dados)
        if afiliado.get('message').__eq__(AfiliadoMessageModel.AFILIADO_JA_EXISTE.value):
            return afiliado, 200
        if not afiliado:
            return {
                'message': AfiliadoMessage.AFILIADO_OCORREU_UM_ERRO_AO_SALVAR.value,
            }, 500
        return {
            'message': AfiliadoMessage.AFILIADO_CRIADO_COM_SUCESSO.value,
            'afiliado': afiliado.json()
        }, 201

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
