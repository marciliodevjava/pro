from enumerate.message import AfiliadoMessage
from enumerate.message import AfiliadoMessageModel
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
        if afiliado.get('message').__eq__(AfiliadoMessageModel.AFILIADO_JA_EXISTE.value):
            return afiliado
        if not afiliado:
            return {
                'message': AfiliadoMessage.AFILIADO_OCORREU_UM_ERRO_AO_SALVAR.value,
            }
        return {
            'message': AfiliadoMessage.AFILIADO_CRIADO_COM_SUCESSO.value,
            'afiliado': afiliado.json()
        }

    @classmethod
    def buscar_afiliado(cls, id):
        afiliado = AfiliadoModel.buscar_afiliado(id)
        if afiliado:
            return {
                'message': AfiliadoMessage.AFILIADO_ENCONTRADO_COM_SUCESSO.value,
                'afiliado': afiliado.json()
            }
        return {
            'message': AfiliadoMessage.AFILIADO_NAO_EXISTE.value
        }

    @classmethod
    def atualizar_afiliado(cls, dados, id):
        afiliado = AfiliadoModel.buscar_afiliado(id)
        if afiliado:
            afiliado = AfiliadoModel.atualizar_afiliado(dados, afiliado)
            if afiliado:
                return {
                    'message': AfiliadoMessage.AFILIADO_ATUALIZADO_COM_SUCESSO.value,
                    'afiliado': afiliado.json()
                }
            return None
        return {
            'message': AfiliadoMessage.AFILIADO_NAO_FOI_ATUALIZADO.value
        }

    @classmethod
    def deletar_afiliado(cls):
        pass
