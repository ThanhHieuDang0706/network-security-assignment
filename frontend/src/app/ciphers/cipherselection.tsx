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
            <div className="mt-4">
                <label className="label">
                    <span className="label-text">Bộ mã</span>
                </label>
                <select className="select w-full max-w-xs select-sm select-bordered" value={cipher} onChange={(e) => setCipher(e.currentTarget.value as CipherType)}>
                    {selections.map((selection, index) => (
                        <option key={selection.value} value={selection.value}>{selection.name}</option>
                    ))}
                </select>
            </div>
        </>
    );
}
