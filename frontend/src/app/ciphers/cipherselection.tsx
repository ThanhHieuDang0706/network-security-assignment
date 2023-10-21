"use client";
import { CipherType } from "@/models/ciphers";
import { useContext } from "react";
import { CipherContext } from "./cipher";

export default function CipherSelection() {

    const { cipher, setCipher } = useContext(CipherContext);

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

    return (
        <>
            <div className="tabs tabs-boxed gap-2 mb-4">
                {
                    selections.map((selection, index) => {
                        return (
                            <a onClick={() => setCipher(selection.value)} className={`tab tab-md ${cipher == selection.value ? "tab-active" : null}`} key={index}>
                                {selection.name}
                            </a>
                        )
                    })
                }
            </div>
        </>
    );
}
