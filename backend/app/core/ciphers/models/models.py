from ..constants import CipherType
from pydantic import BaseModel
from typing import Tuple

class BaseCipherModel(BaseModel):
    type: CipherType

class EncryptionRequest(BaseCipherModel):
    key: int | Tuple[int, ...]
    plain_text: str

class EncryptionResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str

class DecryptionRequest(BaseCipherModel):
    key: int | Tuple[int,...]
    cipher_text: str

class DecryptionResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str

class DecryptionWithoutKeyRequest(BaseCipherModel):
    cipher_text: str

class DecryptionWithoutKeyResponse(BaseModel):
    possible_keys: dict[int | Tuple[int,...], str]

class TryGetCipherKeyRequest(BaseModel):
    plain_text: str
    cipher_text: str

class TryGetCipherKeyResponse(BaseModel):
    plain_text: str
    cipher_text: str
    key: int | Tuple[int, ...]

class CipherResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str
