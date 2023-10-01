from abc import ABC, abstractmethod
import app.core.ciphers.constants as constants

class BaseCipher(ABC):
    def __init__(self):
        self.type = constants.CipherType.BASE

    @abstractmethod
    def encrypt(self, plain_text: str, key = constants.DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    def decrypt(self, plain_text: str, key = constants.DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    def try_decrypt_without_key(self, cipher_text: str) -> dict[int, str]:    
        pass

    @abstractmethod
    def try_get_key(self, plain_text: str, cipher_text: str) -> int:
        pass
    