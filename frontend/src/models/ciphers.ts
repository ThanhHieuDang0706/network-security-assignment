export enum CipherType {
    Caesar = 'cesar',
    RailFence = "rail_fence",
    PermCesarRailFence = "perm_cesar_rail_fence"
}

export interface CipherBase {
    type: CipherType;
}

export interface EncryptionRequest extends CipherBase {
    key: number;
    plain_text: string
}

export interface EncryptionResponse {
    cipher_text: string;
}