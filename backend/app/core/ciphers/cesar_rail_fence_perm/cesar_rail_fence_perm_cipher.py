from app.core.ciphers.base_cipher import BaseCipher
from app.core.ciphers.constants import CipherType
class CesarRailFencePermCipher(BaseCipher):
    def __init__(self):
        self.type = CipherType.PERM_CESAR_RAIL_FENCE

    def encrypt(self, plain_text: str, key: int) -> str:
        pass

    def decrypt(self, cipher_text: str, key: int) -> str:
        pass

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
        pass

    def try_get_key(plain_text: str, cipher_text: str) -> int:
        pass