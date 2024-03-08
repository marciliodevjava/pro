class ProdutoMapper:
    @classmethod
    def mapear_produto(cls, produtos):
        lista_produto = list()
        for produto in produtos:
            lista_produto.append({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'preco': float(produto.preco)
            })
        return lista_produto
