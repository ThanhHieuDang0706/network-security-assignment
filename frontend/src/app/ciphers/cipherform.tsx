"use client"

import { useContext, useEffect, useState } from "react";
import { CipherContext } from "./cipher";
import { encrypt } from "@/services/ciphers";
import Results from "./results";

export default function CipherForm() {
    

    const [result, setResult] = useState("");

    const { cipher, loading, setLoading } = useContext(CipherContext);

    const [input, setInput] = useState({
        content: {
            [cipher]: "",
        },
        key: {
            [cipher]: ""
        },
    });

    const onClickMaHoa = async () => {
        try {
            if (!input.content || !input.key || Number(input.key) <= 0) return alert("Vui lòng nhập đầy đủ thông tin");
            setLoading(true);
            console.log({
                plain_text: input.content[cipher],
                key: parseInt(input.key[cipher]),
                type: cipher
            });
            const value = await encrypt({
                plain_text: input.content[cipher],
                key: parseInt(input.key[cipher]),
                type: cipher
            });
    
            if (value.cipher_text) {
                setResult(value.cipher_text);
            }
        }
        catch (error) {
            
        }
        finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        setInput({
            content: {
                [cipher]: input.content[cipher] || "",
                ...input.content
            },
            key: {
                [cipher]: input.key[cipher] || "",
                ...input.key
            }
        })
    }, [cipher, input.content, input.key])
    
    return (
        <>
            <div className="py-4 form-control">
                <textarea onChange={(event) => { 
                    setInput({
                        ...input,
                        content: {
                            ...input.content,
                            [cipher]: event.currentTarget.value
                        }
                    });     
                }} value={input.content[cipher]} className="textarea h-24 textarea-bordered textarea-sm" placeholder="Nội dung" />
                
                <input value={input.key[cipher]} onChange={(value) => {
                    setInput({
                        ...input,
                        key: {
                            ...input.key,
                            [cipher]: value.currentTarget.value
                        }
                    });
                    

                }} type="number" className="mt-4 w-24 input input-bordered input-sm" placeholder="Khóa" />
            </div>
            <div className="flex gap-2">
                <button disabled={loading} onClick={onClickMaHoa} className="btn btn-sm btn-info text-white">
                    Mã hóa
                </button>
                <button disabled={loading} className="btn btn-sm btn-error text-white">
                    Giải mã
                </button>
            </div>
            {
                loading && (<span className="loading loading-spinner text-accent text-center"></span>)
            }
            {
                result && (
                    <Results results={result} />
                )
            }
        </>
    );
}