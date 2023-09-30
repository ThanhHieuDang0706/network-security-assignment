from abc import ABC, abstractmethod, staticmethod
import backend.app.core.ciphers.constants as constants

class BaseCipher(ABC):
    @abstractmethod
    @staticmethod
    def encrypt(plain_text: str, key = constants.DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    @staticmethod
    def decrypt(plain_text: str, key = constants.DEFAULT_KEY) -> str:
        pass

    @staticmethod
    @abstractmethod
    def try_decrypt_without_key(plain_text: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def try_get_key(plain_text: str, cipher_text: str) -> str:
        pass
    