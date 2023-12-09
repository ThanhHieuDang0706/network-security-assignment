"use client";
import Image from "next/image";
import { CipherType } from "@/models/ciphers";
import { createContext, useState } from "react";
import EncodeCipherForm from "./ciphers/encodecipherform/encodecipherform";
import DecodeCipherForm from "./ciphers/decodercipherform/decodecipherform";
import DecodeWithoutKeyCipherForm from "./ciphers/decodewithoutkeyform/decodewithoutform";
import classNames from "classnames";
import { CipherContext } from "./cipherContext";
import CipherMenu from "./CipherMenu";


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
            <div className="sm:px-0 md:px-32 bg-slate-100 navbar fixed z-50">
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
                <div className="flex-1 gap-4 justify-between sm:justify-between md:justify-normal">
                    <a className="btn btn-ghost normal-case text-xl">Bách Khoa Cipher</a>
                    <nav className="hidden sm:hidden md:block flex-nowrap tabs cursor-pointer flex-3 gap-2">
                        {selections.map((value) => {
                            return (
                                <a
                                    key={value.value}
                                    className={classNames(
                                        "capitalize cursor-pointer tab tab-boredred",
                                        cipher == value.value ? "tab-active tab-border-2 border-b-2 transition-all accent-current" : ""
                                    )}
                                    onClick={(e) => {
                                        e.preventDefault();
                                        e.stopPropagation();
                                        setCipher(value.value);
                                    }}>
                                    {value.name}
                                </a>
                            );
                        })}
                    </nav>
                    <CipherMenu value={cipher} ciphers={selections} onCipherSelected={setCipher} className="sm:flex md:hidden hidden" />
                </div>
            </div>
            <main className="flex bg-slate-50 flex-col md:px-32 md:py-24 card sm:px-2 sm:py-16">
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
