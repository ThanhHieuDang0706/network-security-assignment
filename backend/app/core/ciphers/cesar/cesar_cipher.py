from core.ciphers.base_cipher import BaseCipher
from core.ciphers.constants import CipherType, NOT_FOUND_KEY
import core.ciphers.constants as constants

import string
import re
from core.ciphers.dictionary import load, check, checkCommon, accuracy


class CesarCipher(BaseCipher):
    alphabet = tuple(string.ascii_uppercase)
    SIZE = len(alphabet)

    def __init__(self):
        self.type = constants.CipherType.CESAR

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
        for key in range(1, self.SIZE):
            str = re.sub("[^a-zA-Z ]", "", self.decrypt(cipher_text, key))
            if " " not in str:
                # without spaces
                load("../common.txt")
                flag = checkCommon(str)
            else:
                # with spaces
                load("../dictionary.txt")
                words = str.split()
                flag = accuracy(words)
            if flag == True:
                return {key: self.decrypt(cipher_text, key)}
        return {-1: "NOT_FOUND"}

    def try_get_key(self, plain_text: str, cipher_text: str) -> str:
        keys = list(self.try_decrypt_without_key(cipher_text).keys())
        if keys[0] == -1:
            return NOT_FOUND_KEY
        else:
            return keys[0]
