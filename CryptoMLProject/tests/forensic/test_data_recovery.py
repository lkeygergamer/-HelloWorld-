import unittest
from forensic.data_recovery import recover_data

class TestDataRecovery(unittest.TestCase):
    def test_data_recovery(self):
        recover_data('imagem_disco.img')
        # Adicione verificações para validar a recuperação de dados

if __name__ == '__main__':
    unittest.main()
