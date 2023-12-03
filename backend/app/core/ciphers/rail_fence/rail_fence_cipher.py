from ..base_cipher import BaseCipher
from ..constants import CipherType, NOT_FOUND_KEY, ENGLISH_FREQUENCIES
from ..utils import is_likely_english

PLACE_HOLDER = "$"

class RailFenceCipher(BaseCipher):
    def __init__(self):
        self.type = CipherType.RAIL_FENCE

    def init_rail(self, key: int, text: str) -> list[list[str]]:
        rail = []
        for i in range(key):
            rail.append([])
            for j in range(len(text)):
                rail[i].append(PLACE_HOLDER)
        return rail

    def encrypt(self, plain_text: str, key: int) -> str:
        rail = self.init_rail(key, plain_text)
        go_down = False
        row = 0
        col = 0
        for i in range(len(plain_text)):
            
            if row == 0 or row == key - 1:
                go_down = not go_down

            rail[row][col] = plain_text[i]
            col += 1
            
            if go_down:
                row += 1
            else:
                row -= 1

        result = ""
        for i in range(key):
            for j in range(len(plain_text)):
                if rail[i][j] != PLACE_HOLDER:
                    result += rail[i][j]
        return "".join(result)

    def decrypt(self, cipher_text: str, key: int) -> str:
        rail = self.init_rail(key, cipher_text)
        go_down = False
        
        row = 0
        col = 0
        for i in range(len(cipher_text)):
            if row == 0: 
                go_down = True
            if row == key - 1:
                go_down = False
            
            rail[row][col] = '*'
            col += 1

            if go_down:
                row += 1
            else:
                row -= 1

        """Construct the rail matrix"""
        index = 0
        for i in range(key):
            for j in range(len(cipher_text)):
                if rail[i][j] == '*' and index < len(cipher_text):
                    rail[i][j] = cipher_text[index]
                    index += 1

        result = ""
        row = 0
        col = 0
        for i in range(len(cipher_text)):
            if row == 0:
                go_down = True
            if row == key - 1:
                go_down = False
            
            if rail[row][col] != PLACE_HOLDER:
                result += rail[row][col]
                col += 1
            
            if go_down:
                row += 1
            else:
                row -= 1
                
        return "".join(result)

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
        result = {}
        
        for i in range(2, len(cipher_text)):
            result[i] = self.decrypt(cipher_text, i)

            if (is_likely_english(result[i])):
                return {
                    i: result[i]
                }
            
        return result
    # def try_get_key(self, plain_text: str, cipher_text: str) -> int:
    #     if (len(plain_text) != len(cipher_text)):
    #         return NOT_FOUND_KEY
        
    #     for i in range(2, len(cipher_text)):
    #         if self.decrypt(cipher_text, i) == plain_text:
    #             return i
            
    #     return NOT_FOUND_KEY

        