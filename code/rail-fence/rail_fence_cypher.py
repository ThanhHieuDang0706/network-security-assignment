from base_cypher import BaseCipher

class RailFenceCypher(BaseCipher):
    def encrypt(self, plain_text: str, key: str) -> str:
        pass

    def decrypt(self, plain_text: str, key: str) -> str:
        pass

    def try_decrypt_without_key(plain_text: str) -> str:
        pass

    def try_get_key(plain_text: str, encrypted_text: str) -> str:
        pass