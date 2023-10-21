import { CipherType, EncryptionRequest, EncryptionResponse } from "@/models/ciphers";

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