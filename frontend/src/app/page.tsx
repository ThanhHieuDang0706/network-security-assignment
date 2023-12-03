"use client";
import Image from "next/image";
import { CipherType } from "@/models/ciphers";
import { createContext, useState } from "react";
import EncodeCipherForm from "./ciphers/encodecipherform/encodecipherform";
import DecodeCipherForm from "./ciphers/decodercipherform/decodecipherform";
import DecodeWithoutKeyCipherForm from "./ciphers/decodewithoutkeyform/decodewithoutform";
import classNames from "classnames";

export const CipherContext = createContext({
    cipher: CipherType.Caesar,
    setCipher: (_cipher: CipherType) => {}
});

export default function Home() {
    const selections = [
        {
            name: "Caesar",
            value: CipherType.Caesar
        },
        {
            name: "Rail Fence",
            value: CipherType.RailFence
        },
        {
            name: "Hoán vị Rail Fence & Cipher",
            value: CipherType.PermCesarRailFence
        }
    ];

    const [cipher, setCipher] = useState(CipherType.Caesar);

    return (
        <CipherContext.Provider value={{ cipher, setCipher }}>
            <div className="px-32 bg-slate-100 navbar fixed z-50">
                <div className="flex-none">
                    <a className="btn btn-square btn-ghost">
                        <Image
                            color="#fff"
                            alt="Bách Khoa Cipher"
                            width="24"
                            height="24"
                            className="inline-block w-5 h-5 stroke-current"
                            src="/760px-HCMUT_official_logo.png"
                        />
                    </a>
                </div>
                <div className="flex-1 gap-4">
                    <a className="btn btn-ghost normal-case text-xl">Bách Khoa Cipher</a>
                    <nav className="tabs cursor-pointer flex-1 gap-2 ">
                        {selections.map((value) => {
                            return (
                                <a
                                    key={value.value}
                                    className={classNames(
                                        "capitalize cursor-pointer tab tab-boredred",
                                        cipher == value.value ? "tab-active tab-border-2 border-b-2 transition-all accent-current" : ""
                                    )}
                                    onClick={(e) => {
                                        console.log(e);
                                        e.preventDefault();
                                        e.stopPropagation();
                                        console.log(setCipher);
                                        setCipher(value.value);
                                    }}>
                                    {value.name}
                                </a>
                            );
                        })}
                    </nav>
                </div>
            </div>
            <main className="flex bg-slate-50 flex-col py-24 px-32 card">
                <>
                    <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                        <EncodeCipherForm />
                    </div>

                    <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                        <DecodeCipherForm />
                    </div>

                    <div className="card bg-base-100 shadow-xl min-w-full px-4 my-2">
                        <DecodeWithoutKeyCipherForm />
                    </div>
                </>
            </main>
        </CipherContext.Provider>
    );
}
