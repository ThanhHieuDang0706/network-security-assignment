"use client"

import { useContext, useEffect, useState } from "react";
import { CipherContext } from "../cipher";
import { encrypt } from "@/services/ciphers";
import Results from "./results";

export default function EncodeCipherForm() {
    
    const { cipher, } = useContext(CipherContext);

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState({
        [cipher]: ""
    });


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
            const value = await encrypt({
                plain_text: input.content[cipher],
                key: parseInt(input.key[cipher]),
                type: cipher
            });
    
            if (value.cipher_text) {
                setResult({
                    ...result,
                    [cipher]: value.cipher_text
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
            <h3 className="card-title"> Mã hóa </h3>
            <form onSubmit={(e) => { e.preventDefault(); onClickMaHoa(); }} className="py-4 form-control">
                <textarea required onChange={(event) => { 
                    setInput({
                        ...input,
                        content: {
                            ...input.content,
                            [cipher]: event.currentTarget.value
                        }
                    });     
                }} value={input.content[cipher]} className="textarea h-24 textarea-bordered textarea-sm textarea-info" placeholder="Nội dung" />
                
                <input min="0" required value={input.key[cipher]} onChange={(value) => {
                    setInput({
                        ...input,
                        key: {
                            ...input.key,
                            [cipher]: value.currentTarget.value
                        }
                    });
                    

                }} type="number" className="mt-4 w-24 input input-bordered input-sm input-info" placeholder="Khóa" />
                <div className="mt-4">
                    <button disabled={loading} type="submit" className="btn btn-sm btn-info text-white">
                        Mã hóa
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