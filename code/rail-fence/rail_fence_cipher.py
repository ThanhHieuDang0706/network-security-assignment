from base_cipher import BaseCipher

class RailFenceCipher(BaseCipher):
    def encrypt(plain_text: str, key: str) -> str:
        pass

    def decrypt(plain_text: str, key: str) -> str:
        pass

    def try_decrypt_without_key(plain_text: str) -> str:
        pass

    def try_get_key(plain_text: str, cipher_text: str) -> str:
        pass