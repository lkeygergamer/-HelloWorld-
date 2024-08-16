import unittest
from crypto.encryption import encrypt, decrypt

class TestEncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        message = "Teste"
        encrypted_message = encrypt(message)
        decrypted_message = decrypt(encrypted_message)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
