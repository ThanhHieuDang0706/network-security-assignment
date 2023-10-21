"use client"

import { CipherType } from "@/models/ciphers"
import { createContext, useState } from "react"
import CipherSelection from "./cipherselection";
import CipherForm from "./cipherform";

export const CipherContext = createContext({
    cipher: CipherType.Caesar,
    loading: false,
    setLoading: (loading: boolean) => {},
    setCipher: (cipher: CipherType) => {}
});

export default function CipherProvider() {
    const [cipher, setCipher] = useState(CipherType.Caesar);
    const [loading, setLoading] = useState(false);

    return (
        <CipherContext.Provider value={{ cipher, setCipher, loading, setLoading }}>
            <CipherSelection />
            <CipherForm />
        </CipherContext.Provider>
    );
}