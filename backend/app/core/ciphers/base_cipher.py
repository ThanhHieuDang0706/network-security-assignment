from abc import ABC, abstractmethod
from .constants import CipherType, NOT_FOUND_KEY, DEFAULT_KEY
from typing import Tuple, Union

class BaseCipher(ABC):
    def __init__(self):
        self.type = CipherType.BASE

    @abstractmethod
    def encrypt(self, plain_text: str, key: Union[int, Tuple[int,...]] = DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    def decrypt(self, plain_text: str, key = DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:    
        pass

    # @abstractmethod
    # def try_get_key(self, plain_text: str, cipher_text: str) -> int:
    #     pass
    