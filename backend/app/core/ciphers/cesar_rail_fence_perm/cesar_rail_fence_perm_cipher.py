from ..base_cipher import BaseCipher
from ..constants import CipherType, NOT_FOUND_KEY
from ..cesar.cesar_cipher import CaesarCipher
from ..rail_fence.rail_fence_cipher import RailFenceCipher
from typing import Tuple
class CesarRailFencePermCipher(BaseCipher):
    def __init__(self):
        self.type = CipherType.PERM_CESAR_RAIL_FENCE

    def encrypt(self, plain_text: str, keys: Tuple[int,...]) -> str:
        ceasar_key = keys[0]
        railfence_key = keys[1]
        ceasarText = CaesarCipher()
        ceasarRes = ceasarText.encrypt(plain_text, ceasar_key)
        railfenceText = RailFenceCipher()
        return railfenceText.encrypt(ceasarRes, railfence_key)

    def decrypt(self, cipher_text: str, keys: Tuple[int,...]) -> str:
        ceasarKey = keys[0]
        railfenceKey = keys[1]
        ceasarText = CaesarCipher()
        railfenceText = RailFenceCipher()
        
        railFenceRes = railfenceText.decrypt(cipher_text, railfenceKey)
        ceasarRes = ceasarText.decrypt(railFenceRes, ceasarKey)

        return ceasarRes

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
        ceasarCipher = CaesarCipher()
        railFenceCipher = RailFenceCipher()
        result = {}

        ceasarResults = ceasarCipher.try_decrypt_without_key(cipher_text)
        for ceasarKey in ceasarResults.keys():
            railFenceRes = railFenceCipher.try_decrypt_without_key(ceasarResults[ceasarKey])
            for railFenceKey in railFenceRes.keys():
                result[(ceasarKey, railFenceKey)] = railFenceRes[railFenceKey]
        return result
