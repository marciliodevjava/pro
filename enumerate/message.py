from enum import Enum


class MessageLogin(Enum):
    USUARIO_NAO_EXISTE = 'Usuário não existe, deseja criar esse usuário?'
    LOGIN_SENHA_INCORRETA = 'Senha incorreta, tente novamente.'
    LOGIN_EFETUADO_COM_SUCESSO = 'O Login foi realizado com sucesso.'
    LOGIN_OCORREU_ERRO_AO_LOGAR = 'Ocorreu um erro ao logar, informe ao suporte.'
    LOGIN_USUARIO_DELETADO_COM_SUCESSO = 'Usuário deletado com sucesso.'
    LOGIN_USUARIO_ATUALIZADO_COM_SUCESSO = 'Usuário atualizado com sucesso.'
    LOGIN_USUARIO_CRIADO_COM_SUCESSO = 'Usuário criado com sucesso.'


class MessageToken(Enum):
    TOKEN_INVALIDO = 'O Token é inválido'
    TOKEN_EXPIRADO = 'O Token está expirado.'
    TOKEN_NAO_ENVIADO = 'O Token não foi enviado.'


class UsuarioFormulario(Enum):
    USUARIO_OCORREU_UM_ERRO = 'Ocorreu um erro ao salvar usuario.'
    USUARIO_JA_EXISTE = 'Usuario já existe.'
    USUARIO_CRIADO = 'Usuario criado com sucesso.'
    O_CAMPO_LOGIN = 'O campo login não foi enviado.'
    O_CAMPO_EMAIL = 'O campo email não foi enviado.'
    O_CAMPO_PASSWORD = 'O campo senha não foi enviado.'
    O_CAMPO_USERNAME = 'O campo nome não foi enviado.'


class LoginFormulario(Enum):
    CAMPO_SENHA = 'O campo login não foi enviado.'
    CAMPO_LOGIN = 'O campo senha não foi enviado.'
