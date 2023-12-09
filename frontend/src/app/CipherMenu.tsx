"use client";
import { CipherType } from "@/models/ciphers";


export interface CipherMenuProps {
    className?: string;
    ciphers?: Array<{
        name: string;
        value: CipherType;
    }>;
    onCipherSelected?: (cipher: CipherType) => void;
    value: CipherType;
}

export default function CipherMenu(props: CipherMenuProps) {
    return (
        <select onChange={(e) => {
            if (props.onCipherSelected) {
                props.onCipherSelected(e.target.value as CipherType);
            }
        }} className={"select select-ghost w-full max-w-xs border-none " + props.className}>

            {props.ciphers?.map((cipher) => {
                return (
                    <option
                        key={cipher.value}
                        value={cipher.value}
                        selected={cipher.value == props.value}
                    >
                        {cipher.name}
                    </option>
                );
            })}
        </select>

    );
}