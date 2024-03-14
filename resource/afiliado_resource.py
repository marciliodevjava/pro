from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from enumerate.message import AfiliadoMessageModel, AfiliadoMessage
from form.afiliado_shema import AfiliadoShema
from service.afiliado_service import AfiliadoService


class AfiliadoResource(Resource):

    @jwt_required()
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

    @jwt_required()
    def get(self, id):
        afiliado = AfiliadoService.buscar_afiliado(id)
        if afiliado.get('message').__eq__(AfiliadoMessage.AFILIADO_NAO_EXISTE.value):
            return afiliado, 404
        return afiliado, 200

    @jwt_required()
    def put(self, id):
        dados = AfiliadoShema().load(request.json)
        afiliado = AfiliadoService.atualizar_afiliado(dados, id)
        if afiliado.get('message').__eq__(AfiliadoMessage.AFILIADO_NAO_FOI_ATUALIZADO.value):
            return afiliado, 404
        return afiliado, 200

    @jwt_required()
    def delete(self, id):
        resposta = AfiliadoService.deletar_afiliado(id)
        if resposta:
            return resposta, 200
        return {
            'message': AfiliadoMessage.NAO_FOI_POSSIVEL_DELETAR_AFILIADO.value
        }
