from base_cypher import BaseCipher

class CesarRailFencePermCypher(BaseCipher):
    def encrypt(plain_text: str, key: str) -> str:
        pass

    def decrypt(plain_text: str, key: str) -> str:
        pass

    def try_decrypt_without_key(plain_text: str) -> str:
        pass

    def try_get_key(plain_text: str, encrypted_text: str) -> str:
        pass