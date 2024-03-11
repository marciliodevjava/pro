from repository.afiliado_model import AfiliadoModel
class AfiliadoService:
    @classmethod
    def cadastrar_afiliado(cls, dados):
        nome = dados['nome']
        email = dados['email']
        cpf = dados['cpf']
        rg = dados['rg']
        afiliado = AfiliadoModel(nome, email, cpf, rg)
        afiliado = AfiliadoModel.salvar(afiliado)
        if afiliado:


    @classmethod
    def buscar_afiliado(cls):
        pass

    @classmethod
    def atualizar_afiliado(cls):
        pass

    @classmethod
    def deletar_afiliado(cls):
        pass
