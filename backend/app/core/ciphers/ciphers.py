from typing import List
from backend.app.core.ciphers.cesar.cesar_cipher import CesarCipher
from backend.app.core.ciphers.rail_fence.rail_fence_cipher import RailFenceCipher
from backend.app.core.ciphers.cesar_rail_fence_perm.cesar_rail_fence_perm_cipher import CesarRailFencePermCipher
from backend.app.core.ciphers.base_cipher import BaseCipher

def get_ciphers() -> List[BaseCipher]:
    """
    Returns a list of available ciphers.

    Returns:
        List: A list of available ciphers.
    """
    ciphers = [CesarCipher(), RailFenceCipher(), CesarRailFencePermCipher()]
    return ciphers

def find_ciphers(cipher_type: str) -> List[BaseCipher]:
    """
    Returns cipher object that match the given cipher type.

    Args:
        cipher_type (str): The cipher type to match.

    Returns:
        List: A list of ciphers that match the given cipher type.
    """
    ciphers = get_ciphers()
    return list(filter(lambda cipher: cipher.type == cipher_type, ciphers))