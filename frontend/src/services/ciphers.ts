import { CipherType, DecryptionRequest, DecryptionResponse, DecryptionWithoutKeyRequest, DecryptionWithoutKeyResponse, EncryptionRequest, EncryptionResponse } from "@/models/ciphers";

const baseUrl = process.env.NEXT_PUBLIC_API_URL + "/ciphers";

export const encrypt = async (encryptionRequest: EncryptionRequest): Promise<EncryptionResponse> => {
    const response = await fetch(`${baseUrl}/encrypt`, {
        method: "post",
        body: JSON.stringify(encryptionRequest),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return await response.json();
};

export const decrypt = async (decryptionRequest: DecryptionRequest): Promise<DecryptionResponse> => {
    const response = await fetch(`${baseUrl}/decrypt`, {
        method: "post",
        body: JSON.stringify(decryptionRequest),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return await response.json();
};

export const decryptWithoutKey = async (encryptionRequest: DecryptionWithoutKeyRequest): Promise<DecryptionWithoutKeyResponse> => {
    const response = await fetch(`${baseUrl}/decrypt-without-key`, {
        method: "post",
        body: JSON.stringify(encryptionRequest),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return await response.json();
}