
from ..base_cipher import BaseCipher
from ..constants import CipherType, NOT_FOUND_KEY
from ..utils import is_likely_english
import string


class CesarCipher(BaseCipher):
    alphabet = tuple(string.ascii_uppercase)
    SIZE = len(alphabet)

    def __init__(self):
        self.type = CipherType.CESAR

    def encrypt(self, plain_text: str, key: str) -> str:
        # create sub alphabet
        subAlphabet = []
        for i in range(self.SIZE):
            if i + key >= self.SIZE:
                subAlphabet.append(self.alphabet[key - (self.SIZE - i)])
            else:
                subAlphabet.append(self.alphabet[i + key])

        # create a dict store key = character in alphabet corresponding to value = character in sub alphabet
        arr = {}
        for i in range(self.SIZE):
            arr[f"{self.alphabet[i]}"] = f"{subAlphabet[i]}"
        # string store cipher text
        str = ""
        # start to encrypt
        for i in range(len(plain_text)):
            if plain_text[i].isupper():
                str += arr[f"{plain_text[i]}"]
            elif plain_text[i].islower():
                str += arr[f"{plain_text[i].upper()}"].lower()
            else:
                str += plain_text[i]

        # return value
        return str

    def decrypt(self, cipher_text: str, key: int) -> str:
        return self.encrypt(cipher_text, self.SIZE - key)

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
            """
            Tries to decrypt the given cipher text without knowing the key.
            
            Args:
                cipher_text (str): The cipher text to decrypt.
            
            Returns:
                dict[int, str]: A dictionary containing possible keys and their corresponding decrypted texts.
            """
            result = {}

            # we use frequency analysis to find the key if the cipher_text is long enough
            if (len(cipher_text) > 100):
                # count frequency of each character in the cipher text
                freq = {}
                for i in range(self.SIZE):
                    freq[f"{self.alphabet[i]}"] = cipher_text.lower().count(self.alphabet[i].lower())
                
                # find the most frequent character
                maxFreq = 0
                maxFreqChar = ""
                for i in range(self.SIZE):
                    if freq[self.alphabet[i]] > maxFreq:
                        maxFreq = freq[self.alphabet[i]]
                        maxFreqChar = self.alphabet[i]
                
                # find the key
                key = self.alphabet.index(maxFreqChar) - self.alphabet.index("E")
                if key < 0:
                    key += self.SIZE

                return {
                    key: self.decrypt(cipher_text, key)
                }


            for i in range (1, self.SIZE):
                result[i] = self.decrypt(cipher_text, i)
                
                if (is_likely_english(result[i])):
                    return {
                        i: result[i]
                    }
            return result

    # def try_get_key(self, plain_text: str, cipher_text: str) -> str:
    #     if len(cipher_text) != len(plain_text):
    #         return NOT_FOUND_KEY
        
    #     for i in range(1, self.SIZE):
    #         if plain_text == self.decrypt(cipher_text, i):
    #             return i
        
    #     return NOT_FOUND_KEY


