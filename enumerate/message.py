from enum import Enum

from variables.variaveis_enum import LOGIN, SENHA, EMAIL, NONE, PRECO, DESCRICAO, QUANTIDADE, USUARIO, PRODUTO, TOKEN, \
    CPF, AFILIADO


class MessageLogin(Enum):
    USUARIO_NAO_EXISTE = f'{USUARIO} não existe, deseja criar esse {USUARIO}?'
    LOGIN_SENHA_INCORRETA = 'Senha incorreta, tente novamente.'
    LOGIN_EFETUADO_COM_SUCESSO = 'Login foi realizado com sucesso.'
    LOGIN_OCORREU_ERRO_AO_LOGAR = 'Ocorreu um erro ao logar, informe ao suporte.'
    LOGIN_USUARIO_DELETADO_COM_SUCESSO = f'{USUARIO} deletado com sucesso.'
    LOGIN_USUARIO_ATUALIZADO_COM_SUCESSO = f'{USUARIO} atualizado com sucesso.'
    LOGIN_USUARIO_CRIADO_COM_SUCESSO = f'{USUARIO} criado com sucesso.'


class MessageToken(Enum):
    TOKEN_INVALIDO = f'O {TOKEN} é inválido'
    TOKEN_EXPIRADO = f'O {TOKEN} está expirado.'
    TOKEN_NAO_ENVIADO = f'O {TOKEN} não foi enviado.'
    TOKEN_LOGIN_NOVAMENTE = f'Faça {LOGIN} novamente para obter um novo {TOKEN}'


class UsuarioFormulario(Enum):
    USUARIO_OCORREU_UM_ERRO_PARA_DELETAR = f'Ocorreu um erro ao deletar o {USUARIO}.'
    USUARIO_DELETADO_COM_SUCESSO = f'{USUARIO} deletado com sucesso.'
    USUARIO_NAO_ATUALIZADO = f'{USUARIO} não encontrado para atualizar.'
    USUARIO_ATUALIZADO = f'{USUARIO} atualizado com sucesso.'
    USUARIO_OCORREU_UM_ERRO = f'Ocorreu um erro ao salvar {USUARIO}.'
    USUARIO_JA_EXISTE = f'{USUARIO} já existe.'
    USUARIO_CRIADO = f'{USUARIO} criado com sucesso.'
    O_CAMPO_LOGIN = f'O campo {LOGIN} não foi enviado.'
    O_CAMPO_EMAIL = f'O campo {EMAIL} não foi enviado.'
    O_CAMPO_PASSWORD = f'O campo {SENHA} não foi enviado.'
    O_CAMPO_USERNAME = f'O campo {NONE} não foi enviado.'


class LoginFormulario(Enum):
    CAMPO_SENHA = f'O campo {SENHA} não foi enviado.'
    CAMPO_LOGIN = f'O campo {LOGIN} não foi enviado.'


class ProdutoFormulario(Enum):
    O_CAMPO_PRECO = f'O campo {PRECO} não foi enviado.'
    O_CAMPO_QUANTIDADE = f'O campo {QUANTIDADE} não foi enviado.'
    O_CAMPO_DESCRICAO = f'O campo {DESCRICAO} não foi enviado.'
    O_CAMPO_NOME = f'O campo {NONE} não foi enviado.'


class ProdutoMessage(Enum):
    OCORREU_UM_ERRO_AO_DELETAR_PRODUTO = f'Ocorreu um erro ao deletar o {PRODUTO}.'
    PRODUTO_DELETADO_COM_SUCESSO = f'{PRODUTO} deletado com sucesso.'
    NAO_EXISTE_ESSE_PRODUTO_PARA_ATUALIZAR = f'Não existe esse {PRODUTO} para ser atualizado.'
    OCORREU_UM_ERRO_AO_ATUALIZAR_PRODUTO = f'Ocorreu um erro ao atualizar esse {PRODUTO}.'
    PRODUTO_ATUALIZADO_COM_SUCESSO = f'{PRODUTO} atualizado com sucesso.'
    NAO_EXISTE_PRODUTOS_CADASTRADOS = f'Não existe esse {PRODUTO} cadastrados.'
    PRODUTO_OCORREU_UM_ERRO = f'Ocorreu um erro ao salvar {PRODUTO}.'
    PRODUTO_CRIADO_COM_SUCESSO = f'{PRODUTO} criado com sucesso.'
    PRODUTO_EXISTENTE = f'Esse {PRODUTO} já foi cadastrado.'


class ErroServidorMessage(Enum):
    ERRO_OCORREU_ERRO_INTERNO_SERVIDOR = 'Ocorreu um erro interno no servidor.'
    ERRO_INTERNO_SERVIDOR = 'Erro interno no servidor'


class AfiliadoFormulario(Enum):
    CAMPO_PRECO = f'O campo {PRECO} não foi enviado.'
    CAMPO_CPF = f'O campo {CPF} não foi enviado.'
    CAMPO_EMAIL = f'O campo {EMAIL} não foi enviado.'
    CAMPO_NOME = f'O campo {NONE} não foi enviado.'


class AfiliadoMessage(Enum):
    AFILIADO_NAO_EXISTE = f'A busca não encontrou esse {AFILIADO}.'
    AFILIADO_ENCONTRADO_COM_SUCESSO = f'{AFILIADO} encontrado com sucesso.'
    AFILIADO_OCORREU_UM_ERRO_AO_SALVAR = f'Ocorreu um erro ao salvar {AFILIADO}.'
    AFILIADO_CRIADO_COM_SUCESSO = f'{AFILIADO} criado com sucesso.'


class AfiliadoMessageModel(Enum):
    AFILIADO_JA_EXISTE = f"{AFILIADO} já existe."
