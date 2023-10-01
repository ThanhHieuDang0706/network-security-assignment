from backend.app.core.ciphers.base_cipher import BaseCipher
from backend.app.core.ciphers.constants import CipherType 
from typing import dict

class RailFenceCipher(BaseCipher):
    def __init__(self):
        self.type = CipherType.RAIL_FENCE

    def encrypt(self, plain_text: str, key: int) -> str:
        rail = [['\n' for i in range(len(plain_text))] * key]
        go_down = False
        row = 0
        for colIndex in range(plain_text):
            rail[row][colIndex] = plain_text[colIndex]
            if row == 0 or row == key - 1:
                go_down = not go_down
            if go_down:
                row += 1
            else:
                row -= 1

        result = ""
        for i in range(key):
            for j in range(len(plain_text)):
                if rail[i][j] != '\n':
                    result += rail[i][j]

        return "".join(result)

    def decrypt(self, cipher_text: str, key: int) -> str:
        rail = [['\n' for i in range(len(cipher_text))] * key]
        go_down = False

        for colIndex in range(len(cipher_text)):
            rail[row][colIndex] = '*'
            if row == 0 or row == key - 1:
                go_down = not go_down
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
        for colIndex in range(len(cipher_text)):
            if row == 0 or row == key - 1:
                go_down = not go_down
            result += rail[row][colIndex]
            if go_down:
                row += 1
            else:
                row -= 1

        return "".join(result)

    def try_decrypt_without_key(self, plain_text: str) -> dict[int, str]:
        result = []
        for i in range(2, len(plain_text)):
            result.append(self.decrypt(plain_text, i))

    def try_get_key(self, plain_text: str, cipher_text: str) -> int:
        decrypted_results = self.try_decrypt_without_key(cipher_text)
        for i in range(len(decrypted_results)):
            if decrypted_results[i] == plain_text:
                """The key is i + 2 because the key starts at 2 and not 0"""
                return i + 2