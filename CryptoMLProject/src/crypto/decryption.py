from cryptography.fernet import Fernet

def decrypt(encrypted_message: bytes) -> str:
    """Descriptografa uma mensagem"""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
