/* eslint-disable no-unused-vars */
export enum CipherType {
    Caesar = 'cesar',
    RailFence = "rail_fence",
    PermCesarRailFence = "perm_cesar_rail_fence"
}

export interface CipherBase {
    type: CipherType;
}

export interface EncryptionRequest extends CipherBase {
    key: number | [number, number];
    plain_text: string
}

export interface EncryptionResponse extends CipherBase {
    cipher_text: string;
    plain_text: string;
}

export interface DecryptionRequest extends CipherBase {
    key: number | [number, number];
    cipher_text: string
}

export interface DecryptionResponse extends CipherBase {
    plain_text: string;
    cipher_text: string;
}

export interface DecryptionWithoutKeyRequest extends CipherBase {
    cipher_text: string
}

export interface DecryptionWithoutKeyResponse {
    possible_keys: {
        [key: number]: string;
        [keyTuple: string]: string;
    }
}