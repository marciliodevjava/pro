from enum import Enum


class MessageLogin(Enum):
    LOGIN_EFETUADO_COM_SUCESSO = 'O Login foi realizado com sucesso.'
    LOGIN_OCORREU_ERRO_AO_LOGAR = 'Ocorreu um erro ao logar, informe ao suporte.'
    LOGIN_USUARIO_DELETADO_COM_SUCESSO = 'Usuário deletado com sucesso'
    LOGIN_USUARIO_ATUALIZADO_COM_SUCESSO = 'Usuário atualizado com sucesso'
    LOGIN_USUARIO_CRIADO_COM_SUCESSO = 'Usuário criado com sucesso'
