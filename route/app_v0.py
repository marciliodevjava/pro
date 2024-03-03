from flask_restful import Api

from resource.login_resource import Login
from variaveis.variaves import BASE_PATH_HTTP


def config_routes_v0(api: Api):
    api.add_resource(Login, f'{BASE_PATH_HTTP}/login', methods=["GET"], endpoint='get')
    api.add_resource(Login, f'{BASE_PATH_HTTP}/cadastro', methods=["POST"], endpoint='post')
    api.add_resource(Login, f'{BASE_PATH_HTTP}/login', methods=["PUT"], endpoint='put')
    api.add_resource(Login, f'{BASE_PATH_HTTP}/login', methods=["DELETE"], endpoint='delete')
    return api
