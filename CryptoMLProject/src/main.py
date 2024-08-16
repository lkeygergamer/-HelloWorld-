from crypto.encryption import encrypt
from crypto.decryption import decrypt
from steganography.image_steganography import encode_image
from ml.model_training import train_model
from forensic.data_recovery import recover_data

def main():
    print("CryptoMLProject iniciado")

    # Exemplo de criptografia e descriptografia
    message = "Mensagem Secreta"
    encrypted_message = encrypt(message)
    print(f"Mensagem Criptografada: {encrypted_message}")
    decrypted_message = decrypt(encrypted_message)
    print(f"Mensagem Descriptografada: {decrypted_message}")

    # Exemplo de esteganografia
    encode_image('imagem_original.png', message, 'imagem_codificada.png')
    print("Mensagem codificada na imagem.")

    # Exemplo de treinamento de modelo
    # Dados fictícios
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    y = [0, 1, 0, 1]
    model = train_model(X, y)

    # Exemplo de recuperação de dados
    recover_data('imagem_disco.img')

if __name__ == "__main__":
    main()
