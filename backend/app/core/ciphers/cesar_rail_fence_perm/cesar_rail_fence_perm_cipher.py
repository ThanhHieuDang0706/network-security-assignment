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
        ceasarTest = CesarCipher()
        railfenceTest = RailFenceCipher()
        for i in range (2, len(cipher_text)):
            for j in range(1, ceasarTest.SIZE):
                res = railfenceTest.decrypt(cipher_text, i)
                result = ceasarTest.try_decrypt_without_key(res)
                ckey = list(result.keys())
                if ckey[0] != -1:
                    return {(i, ckey[0]): result[ckey[0]]}
            return {-1: "NOT_FOUND"}

    def try_get_key(self, cipher_text: str) -> tuple[int, int]:       
        keys = list(self.try_decrypt_without_key(cipher_text).keys())
        if keys[0] == -1:
            return NOT_FOUND_KEY
        else:
            return keys[0]