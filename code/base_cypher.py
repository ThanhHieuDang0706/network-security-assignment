from abc import ABC, abstractmethod, staticmethod
import constants

class BaseCipher(ABC):
    @abstractmethod
    @staticmethod
    def encrypt(plain_text: str, key: str = constants.DEFAULT_KEY) -> str:
        pass

    @abstractmethod
    @staticmethod
    def decrypt(plain_text: str, key: str = constants.DEFAULT_KEY) -> str:
        pass

    @staticmethod
    @abstractmethod
    def try_decrypt_without_key(plain_text: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def try_get_key(plain_text: str, encrypted_text: str) -> str:
        pass
    