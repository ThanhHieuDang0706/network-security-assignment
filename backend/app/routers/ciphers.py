from fastapi import APIRouter, HTTPException, status
from core.ciphers.models.models import EncryptionRequest, DecryptionRequest, DecryptionWithoutKeyRequest, TryGetCipherKeyRequest, CipherResponse, DecryptionWithoutKeyResponse, EncryptionResponse, DecryptionResponse
from core.ciphers.ciphers import find_cipher
from fastapi.responses import JSONResponse as J

router = APIRouter(
    prefix="/ciphers",
    tags=["ciphers"],
    responses={404: {"description": "Not found"}},
)

@router.post("/encrypt", response_model=EncryptionResponse)
async def encrypt(request: EncryptionRequest):
    """Encrypts a plain text with a key using a cipher"""
    try:
        cipher = find_cipher(request.type)

        if (cipher is None):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cipher not found")
        cipher_text = cipher.encrypt(request.plain_text, request.key)

        return EncryptionResponse(type=request.type, cipher_text=cipher_text, plain_text=request.plain_text)
        
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.post("/decrypt", response_model=DecryptionResponse)
async def decrypt(request: DecryptionRequest):
    """Decrypts a cipher text with a key using a cipher"""
    try:
        cipher = find_cipher(request.type)
        if (cipher is None):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cipher not found")
    
        plain_text = cipher.decrypt(request.cipher_text, request.key)

        return DecryptionResponse(type=request.type, cipher_text=request.cipher_text, plain_text=plain_text)        
    except Exception as e: 
        print(e)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.post("/decrypt-without-key")
async def decrypt_without_key(request: DecryptionWithoutKeyRequest):
    """Decrypts a cipher text without a key using a cipher"""
    try:
        cipher = find_cipher(request.type)
        if (cipher is None):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cipher not found")
    
        possible_keys = cipher.decrypt_without_key(request.cipher_text)
        return DecryptionWithoutKeyResponse(cipher_text=request.cipher_text, possible_keys=possible_keys)
        
    except Exception as e: 
        print(e)
        return J(HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error"))

@router.post("/try-get-key")
async def try_get_key(request: TryGetCipherKeyRequest):
    """Tries to get the key used to encrypt a plain text into a cipher text using a cipher"""
    try:
        cipher = find_cipher(request.type)
        if (cipher is None):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cipher not found")
    
        key = cipher.try_get_key(request.plain_text, request.cipher_text)
        return CipherResponse(type=request.type, key=key, cipher_text=request.cipher_text, plain_text=request.plain_text),
        
    except Exception as e: 
        print(e)
        return J(HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error"))
