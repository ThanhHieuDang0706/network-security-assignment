"use client"
import { useContext, useEffect, useState } from "react";
import { decryptWithoutKey } from "@/services/ciphers";
import Results from "./results";
import { CipherContext } from "@/app/page";

export default function DecodeWithoutKeyCipherForm() {
    
    const { cipher } = useContext(CipherContext);

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState({
        [cipher]: {}
    });


    const [input, setInput] = useState({
        content: {
            [cipher]: "",
        },
        key: {
            [cipher]: ""
        },
    });

    const onClickGiaiMa = async () => {
        try {
            if (!input.content || !input.key || Number(input.key) <= 0) return alert("Vui lòng nhập đầy đủ thông tin");
            setLoading(true);
            const value = await decryptWithoutKey({
                cipher_text: input.content[cipher],
                type: cipher
            });
    
            if (value.possible_keys) {
                setResult({
                    ...result,
                    [cipher]: value.possible_keys
                });
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
        });
    }, [cipher])
    
    return (
        <div className=" py-4 ">
            <h3 className="card-title"> Giải mã không khóa </h3>
            <form onSubmit={(e) => { e.preventDefault(); onClickGiaiMa(); }} className="py-4 form-control">
                <textarea required onChange={(event) => { 
                    setInput({
                        ...input,
                        content: {
                            ...input.content,
                            [cipher]: event.currentTarget.value
                        }
                    });     
                }} value={input.content[cipher]} className="textarea h-24 textarea-bordered textarea-sm textarea-warning" placeholder="Bản mã" />
                
                <div className="mt-4">
                    <button disabled={loading} type="submit" className="btn btn-sm btn-warning text-white">
                        Giải mã
                    </button>
                </div>
            </form>
            {
                result[cipher] && (
                    <Results loading={loading} results={result[cipher]} />
                )
            }
        </div>
    );
}