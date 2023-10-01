from app.core.ciphers.base_cipher import BaseCipher
import app.core.ciphers.constants as constants

class CesarCipher(BaseCipher):
    def __init__(self):
        self.type = constants.CipherType.CESAR

    def encrypt(self, plain_text: str, key: str) -> str:
        pass

    def decrypt(self, cipher_text: str, key: str) -> str:
        pass

    def try_decrypt_without_key(self, plain_text: str) -> dict[int, str]:
        pass

    def try_get_key(self, plain_text: str, cipher_text: str) -> str:
        pass