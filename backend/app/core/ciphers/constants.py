from enum import Enum

DEFAULT_KEY = 1

NOT_FOUND_KEY = -1

class CipherType(str, Enum):
    BASE = "base",
    CESAR = "cesar",
    RAIL_FENCE = "rail_fence",
    PERM_CESAR_RAIL_FENCE = "perm_cesar_rail_fence",