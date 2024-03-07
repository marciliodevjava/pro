from flask_restful import Api

from resource.login_resource import CadastroResource, LoginResource
from resource.produto_resource import ProdutoResource
from variaveis.variaves import BASE_PATH_HTTP


def config_routes_v0(api: Api):
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["POST"], endpoint='cadastro_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["PUT"], endpoint='alterar_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["DELETE"], endpoint='deletar_usuario')
    api.add_resource(LoginResource, f'{BASE_PATH_HTTP}/login', methods=["POST"], endpoint='login')

    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['POST'], endpoint='cadastro_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['PUT'], endpoint='alterar_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['GET'], endpoint='buscar_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['DELETE'], endpoint='deletar_produto')
    return api
