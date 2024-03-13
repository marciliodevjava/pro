from enumerate.message import AfiliadoMessage
from repository.afiliado_model import AfiliadoModel
from utils.formatador_utils import FormatadorDados

class AfiliadoService:
    @classmethod
    def cadastrar_afiliado(cls, dados):
        nome = FormatadorDados.formatador_nome(dados['nome'])
        email = FormatadorDados.formatador_email(dados['email'])
        cpf = FormatadorDados.formatar_cpf(dados['cpf'])
        rg = FormatadorDados.formatar_rg(dados['rg'])
        afiliado = AfiliadoModel(nome, email, cpf, rg)
        afiliado = AfiliadoModel.salvar(afiliado)
        if not afiliado:
            return {
                'message': AfiliadoMessage.AFILIADO_OCORREU_UM_ERRO_AO_SALVAR.value,
            }
        return {
            'message': AfiliadoMessage.AFILIADO_CRIADO_COM_SUCESSO.value,
            'afiliado': afiliado.json()
        }

    @classmethod
    def buscar_afiliado(cls):
        pass

    @classmethod
    def atualizar_afiliado(cls):
        pass

    @classmethod
    def deletar_afiliado(cls):
        pass
