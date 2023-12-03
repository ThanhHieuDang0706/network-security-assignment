import { CipherType } from "@/models/ciphers";
import { createContext } from "react";

export const CipherContext = createContext({
    cipher: CipherType.Caesar,
    setCipher: (_cipher: CipherType) => {}
});