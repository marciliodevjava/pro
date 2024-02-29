from flask_restful import Api

from variaveis.variaves import DATABASE_URI, SQLALCHEMY_DATABASE_URI, HEADER_NAME, HEADER_TYPE, NM_ID_SESSAO, NONE


def config_app(api: Api):
    api.app.config[DATABASE_URI] = SQLALCHEMY_DATABASE_URI
    api.app.config[HEADER_NAME] = NM_ID_SESSAO
    api.app.config[HEADER_TYPE] = NONE
    return api
