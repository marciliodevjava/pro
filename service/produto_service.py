from enumerate.message import ProdutoMessage
from repository.produto_model import ProdutoModel


class ProdutoService:

    @classmethod
    def cadastro_produto(cls, dados):
        produto = ProdutoModel.buscar_produto(dados['nome'], dados['descricao'])
        if produto:
            return {
                'message': ProdutoMessage.PRODUTO_EXISTENTE.value
            }
        nome = dados['nome']
        descricao = dados['descricao']
        quantidade = dados['quantidade']
        preco = dados['preco']
        produto = ProdutoModel(nome=nome, descricao=descricao, quantidade=quantidade, preco=preco)

        try:
            produto = ProdutoModel.salvar(produto)
            if produto:
                return {
                    'message': ProdutoMessage.PRODUTO_CRIADO_COM_SUCESSO.value,
                    'produto': produto.json()
                }
        except Exception as e:
            return None

    @classmethod
    def buscar_todos(cls):
        produto = ProdutoModel.buscar_todos_produtos()
        return produto
