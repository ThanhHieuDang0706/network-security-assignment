from abc import ABC, abstractmethod
from .constants import CipherType, NOT_FOUND_KEY, DEFAULT_KEY
from typing import Tuple, Union

class BaseCipher(ABC):
    def __init__(self):
        self.type = CipherType.BASE

    @abstractmethod
    def encrypt(self, plain_text: str, key: Union[int, Tuple[int,...]] = DEFAULT_KEY) -> str:
            """
            Encrypts the given plain text using the specified key.

            Args:
                plain_text (str): The plain text to be encrypted.
                key (Union[int, Tuple[int,...]]): The encryption key. Defaults to DEFAULT_KEY.

            Returns:
                str: The encrypted text.
            """
            pass

    @abstractmethod
    def decrypt(self, plain_text: str, key = DEFAULT_KEY) -> str:
            """
            Decrypts the given plain text using the specified key.

            Args:
                plain_text (str): The text to be decrypted.
                key (str): The encryption key. Defaults to DEFAULT_KEY.

            Returns:
                str: The decrypted text.
            """
            pass

    @abstractmethod
    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:
            """
            Tries to decrypt the given cipher text without a key.

            Args:
                cipher_text (str): The cipher text to decrypt.

            Returns:
                dict[int, str]: A dictionary containing possible decryption results, where the key is the attempt number and the value is the decrypted text.
            """
            pass

    # @abstractmethod
    # def try_get_key(self, plain_text: str, cipher_text: str) -> int:
    #     pass
    