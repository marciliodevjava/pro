from repository.produto_model import ProdutoModel
from enumerate.message import ProdutoMessage
class ProdutoService:

    @classmethod
    def cadastro_produto(cls, dados):
        produto = ProdutoModel.buscar_produto(dados['nome'], dados['descricao'])
        if produto:
            return {
                'message': ProdutoMessage.PRODUTO_EXISTENTE.value
            }