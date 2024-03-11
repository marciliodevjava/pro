from flask_restful import Api

from resource.login_resource import CadastroResource, LoginResource
from resource.produto_resource import ProdutoResource
from resource.afiliados_resource import AfiliadoResource
from variables.variaves_do_sistema import BASE_PATH_HTTP


def config_routes_v0(api: Api):
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["POST"], endpoint='cadastro_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["PUT"], endpoint='alterar_usuario')
    api.add_resource(CadastroResource, f'{BASE_PATH_HTTP}/cadastro', methods=["DELETE"], endpoint='deletar_usuario')
    api.add_resource(LoginResource, f'{BASE_PATH_HTTP}/login', methods=["POST"], endpoint='login')

    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['POST'], endpoint='cadastro_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto/<int:id>', methods=['PUT'], endpoint='alterar_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto', methods=['GET'], endpoint='buscar_produto')
    api.add_resource(ProdutoResource, f'{BASE_PATH_HTTP}/produto/<int:id>', methods=['DELETE'], endpoint='deletar_produto')

    api.add_resource(AfiliadoResource, f'{BASE_PATH_HTTP}/afiliado', methods=['POST'], endpoint='cadastro_afiliado')
    api.add_resource(AfiliadoResource, f'{BASE_PATH_HTTP}/afiliado', methods=['PUT'], endpoint='alterar_afiliado')
    api.add_resource(AfiliadoResource, f'{BASE_PATH_HTTP}/afiliado/<int:id>', methods=['GET'], endpoint='buscar_afiliado')
    api.add_resource(AfiliadoResource, f'{BASE_PATH_HTTP}/afiliado', methods=['DELETE'], enpoint='deletar_afiliado')
    return api
