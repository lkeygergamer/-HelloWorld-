from cryptography.fernet import Fernet

def generate_key():
    """Gera uma nova chave e a salva em um arquivo"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carrega a chave do arquivo"""
    return open("secret.key", "rb").read()
