import bcrypt


def gerador_password_hash(password):
    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hash_password


def check_password_hash(user_password, banco_password):
    valida = bcrypt.checkpw(user_password.encode('utf-8'), banco_password.encode('utf-8'))
    return valida
