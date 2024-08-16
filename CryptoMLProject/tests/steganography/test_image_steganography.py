import unittest
from steganography.image_steganography import encode_image

class TestImageSteganography(unittest.TestCase):
    def test_image_encoding(self):
        encode_image('imagem_original.png', 'Mensagem Secreta', 'imagem_codificada.png')
        # Adicione verificações para validar a codificação

if __name__ == '__main__':
    unittest.main()
