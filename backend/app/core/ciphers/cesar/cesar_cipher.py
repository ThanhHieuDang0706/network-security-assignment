
from ..base_cipher import BaseCipher
from ..constants import CipherType, MIN_CHARS_TO_DO_FREQUENCY_ANALYSIS
from ..utils import is_likely_english
import string
from collections import Counter


class CaesarCipher(BaseCipher):
    alphabet = tuple(string.ascii_uppercase)
    ALPHABET_SIZE = len(alphabet)

    def __init__(self):
        self.type = CipherType.CESAR

    def get_same_case_alphabet(self, letterToTransform: str, targetLetter: str) -> str:
        if targetLetter.isupper():
            return letterToTransform.upper()
        else:
            return letterToTransform.lower()

    def encrypt(self, plain_text: str, key: str) -> str:
        sub_alphabet = [self.alphabet[(i + key) % self.ALPHABET_SIZE] for i in range(self.ALPHABET_SIZE)]
        mapping = {self.alphabet[i]: sub_alphabet[i] for i in range(self.ALPHABET_SIZE)}
        return ''.join(self.get_same_case_alphabet(mapping[c.upper()], c) if c.isalpha() else c for c in plain_text)

    def decrypt(self, cipher_text: str, key: int) -> str:
        return self.encrypt(cipher_text, self.ALPHABET_SIZE - key)

    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
            result = {}

            # we use frequency analysis to find the key if the cipher_text is long enough
            if len(cipher_text) > MIN_CHARS_TO_DO_FREQUENCY_ANALYSIS:
                char_frequency = Counter(char.lower() for char in cipher_text if char != ' ')
                max_freq_char = char_frequency.most_common(1)[0][0]
                if (max_freq_char.upper() == 'E'):
                    key = (self.alphabet.index(max_freq_char.upper()) - self.alphabet.index("E")) % self.ALPHABET_SIZE
                    result = {key: self.decrypt(cipher_text, key)}
                    return result

            # if the cipher_text is short, we try all possible keys
            for i in range(1, self.ALPHABET_SIZE):
                result[i] = self.decrypt(cipher_text, i)
                if is_likely_english(result[i]):
                    return {i: result[i]}

            return result


