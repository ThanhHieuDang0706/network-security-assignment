from ..base_cipher import BaseCipher
from ..constants import CipherType, NOT_FOUND_KEY
from ..cesar.cesar_cipher import CaesarCipher
from ..rail_fence.rail_fence_cipher import RailFenceCipher
from typing import Tuple
from ..utils import is_likely_english

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

        for railFenceKey in range(2, len(cipher_text) // 2 + 1):
            railFenceRes = railFenceCipher.decrypt(cipher_text, railFenceKey)
            ceasarRes = ceasarCipher.try_decrypt_without_key(railFenceRes)
            
            if len(ceasarRes) == 1:
                item = list(ceasarRes.items())[0]
                if is_likely_english(item[1]):
                    return {
                        (item[0], railFenceKey): item[1]
                    }
            else:
                for ceasarKey in ceasarRes.keys():
                    result[(ceasarKey, railFenceKey)] = ceasarRes[ceasarKey]
