from flask_restful import Api

from resource.login_resource import CadastroResource, LoginResource
from variaveis.variaves import BASE_PATH_HTTP


def config_routes_v0(api: Api):
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["POST"], endpoint='cadastro_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["PUT"], endpoint='alterar_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["DELETE"], endpoint='deletar_usuario')
    api.add_resource(LoginResource, f'{BASE_PATH_HTTP}/login', methods=["POST"], endpoint='login')
    return api
