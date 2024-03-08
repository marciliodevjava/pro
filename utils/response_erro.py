from flask import jsonify

from enumerate.message import MessageToken, ErroServidorMessage


class ResponseErro:

    @classmethod
    def token_expirado(cls):
        return jsonify({
            'error': MessageToken.TOKEN_EXPIRADO.value,
            'message': MessageToken.TOKEN_LOGIN_NOVAMENTE.value
        })

    @classmethod
    def http_exception(cls):
        return jsonify({
            'error': ErroServidorMessage.ERRO_INTERNO_SERVIDOR.value,
            'message': ErroServidorMessage.ERRO_OCORREU_ERRO_INTERNO_SERVIDOR.value
        })
