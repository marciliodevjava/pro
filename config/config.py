from flask_restful import Api

from config.banco_de_dados import db
from config.jwt import jwt
from variaveis.variaves import DATABASE_URI, SQLALCHEMY_DATABASE_URI, HEADER_NAME, HEADER_TYPE, NM_ID_SESSAO, NONE


def config_app(api: Api):
    api.app.config[DATABASE_URI] = SQLALCHEMY_DATABASE_URI
    api.app.config[HEADER_NAME] = NM_ID_SESSAO
    api.app.config[HEADER_TYPE] = NONE

    db.init_app(api.app)
    jwt.init_app(api.app)

    return api
