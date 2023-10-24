from core.ciphers.constants import CipherType
from pydantic import BaseModel
from typing import Optional

class BaseCipherModel(BaseModel):
    type: CipherType

class EncryptionRequest(BaseCipherModel):
    key: int
    plain_text: str

class EncryptionResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str

class DecryptionRequest(BaseCipherModel):
    key: int
    cipher_text: str

class DecryptionResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str

class DecryptionWithoutKeyRequest(BaseCipherModel):
    cipher_text: str

class DecryptionWithoutKeyResponse(BaseModel):
    possible_keys: dict[int, str]

class TryGetCipherKeyRequest(BaseModel):
    plain_text: str
    cipher_text: str

class TryGetCipherKeyResponse(BaseModel):
    plain_text: str
    cipher_text: str
    key: int

class CipherResponse(BaseCipherModel):
    cipher_text: str
    plain_text: str
