from typing import List
from .cesar.cesar_cipher import CaesarCipher
from .rail_fence.rail_fence_cipher import RailFenceCipher
from .cesar_rail_fence_perm.cesar_rail_fence_perm_cipher import CesarRailFencePermCipher
from .base_cipher import BaseCipher

def get_ciphers() -> List[BaseCipher]:
    """
    Returns a list of available ciphers.

    Returns:
        List: A list of available ciphers.
    """
    ciphers = [CaesarCipher(), RailFenceCipher(), CesarRailFencePermCipher()]
    return ciphers

def find_cipher(cipher_type: str) -> BaseCipher:
    """
    Returns cipher object that match the given cipher type.

    Args:
        cipher_type (str): The cipher type to match.

    Returns:
        List: A list of ciphers that match the given cipher type.
    """
    ciphers = get_ciphers()
    result = list(filter(lambda cipher: cipher.type == cipher_type, ciphers))
    if (len(result) == 0):
        return None
    return result[0]