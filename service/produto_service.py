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

    @classmethod
    def atualizar_produto(cls, dados, identification):
        produto = ProdutoModel.buscar_produto_id(identification)
        if produto:
            produto = ProdutoModel.atualizar_produto(produto, dados)
            if produto:
                return {
                    'message': ProdutoMessage.PRODUTO_ATUALIZADO_COM_SUCESSO.value,
                    'produto': produto.json()
                }
            return {
                'message': ProdutoMessage.OCORREU_UM_ERRO_AO_ATUALIZAR_PRODUTO.value
            }
        return {
            'message': ProdutoMessage.NAO_EXISTE_ESSE_PRODUTO_PARA_ATUALIZAR.value
        }
