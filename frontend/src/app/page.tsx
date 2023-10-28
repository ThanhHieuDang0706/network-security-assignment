"use client";
import Image from "next/image";
import { CipherType } from "@/models/ciphers";
import { ReactNode, createContext, useContext, useState } from "react";
import EncodeCipherForm from "./ciphers/encodecipherform/encodecipherform";
import DecodeCipherForm from "./ciphers/decodercipherform/decodecipherform";
import DecodeWithoutKeyCipherForm from "./ciphers/decodewithoutkeyform/decodewithoutform";

export const CipherContext = createContext({
    cipher: CipherType.Caesar,
    setCipher: (cipher: CipherType) => {}
});

export function CipherProvider(props: { chidren: ReactNode }) {
    const [cipher, setCipher] = useState(CipherType.Caesar);

    return <CipherContext.Provider value={{ cipher, setCipher }}>{props.chidren}</CipherContext.Provider>;
}

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

    const { cipher, setCipher } = useContext(CipherContext);

    return (
        <>
            <div className="px-32 bg-slate-100 navbar bg-base-100 fixed z-50">
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
                    <div className="tabs flex-1 gap-4">
                        {selections.map((value) => {
                            return (
                                <a
                                    key={value.value}
                                    className={"capitalize cursor-pointer tab tab-boredred" + value.value == cipher ? "tab-active" : ""}
                                    onClick={(item) => {
                                        item.preventDefault();
                                        item.stopPropagation();
                                        setCipher(value.value);
                                    }}>
                                    {value.name}
                                </a>
                            );
                        })}
                    </div>
                </div>
            </div>
            <main className="flex bg-slate-50 flex-col py-16 px-32 card">
                <CipherContext.Provider value={{ cipher, setCipher }}>
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
            </main>
        </>
    );
}
