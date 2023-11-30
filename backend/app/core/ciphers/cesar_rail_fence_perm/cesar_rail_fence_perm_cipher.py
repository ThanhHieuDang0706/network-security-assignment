from core.ciphers.base_cipher import BaseCipher
from core.ciphers.constants import CipherType, NOT_FOUND_KEY
from core.ciphers.cesar.cesar_cipher import CesarCipher
from core.ciphers.rail_fence.rail_fence_cipher import RailFenceCipher
class CesarRailFencePermCipher(BaseCipher):
    def __init__(self):
        self.type = CipherType.PERM_CESAR_RAIL_FENCE

    def encrypt(self, plain_text: str, ckey: int, rkey: int) -> str:
        ceasarText = CesarCipher()
        railfenceText = RailFenceCipher()
        ceasarRes = ceasarText.encrypt(plain_text, ckey)
        return railfenceText.encrypt(ceasarRes, rkey)

    def decrypt(self, cipher_text: str, ckey: int, rkey) -> str:
        ceasarText = CesarCipher()
        railfenceText = RailFenceCipher()
        raifenceRes = railfenceText.decrypt(cipher_text, rkey)
        return ceasarText.decrypt(raifenceRes, ckey)

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
        ceasarText = CesarCipher()
        result = {}
        for i in range (2, len(cipher_text)):
            for j in range(1, ceasarText.SIZE):
                result[(i, j)] = self.decrypt(cipher_text, j, i)
        return result

    def try_get_key(self, plain_text: str, cipher_text: str) -> int:
        if len(plain_text) != len(cipher_text):
            return KEY_NOT_FOUND
        
        for i in range (2, len(cipher_text)):
            for j in range(1, ceasarText.SIZE):
                if plain_text == self.decrypt(cipher_text, j, i):
                    return (i, j)
        return KEY_NOT_FOUND