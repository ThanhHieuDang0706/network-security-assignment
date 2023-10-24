"use client"

import { CipherType } from "@/models/ciphers"
import { createContext, useState } from "react"
import CipherSelection from "./cipherselection";
import EncodeCipherForm from "./encodecipherform/encodecipherform";
import DecodeCipherForm from "./decodercipherform/decodecipherform";
import DecodeWithoutKeyCipherForm from "./decodewithoutkeyform/decodewithoutform";

export const CipherContext = createContext({
    cipher: CipherType.Caesar,
    setCipher: (cipher: CipherType) => {}
});

export default function CipherProvider() {
    const [cipher, setCipher] = useState(CipherType.Caesar);

    return (
        <CipherContext.Provider value={{ cipher, setCipher }}>
            <div className="my-2 px-2">
                <CipherSelection />
            </div>
            <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                <EncodeCipherForm />
            </div>

            <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                <DecodeCipherForm />
            </div>

            <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                <DecodeWithoutKeyCipherForm />
            </div>
        </CipherContext.Provider>
    );
}