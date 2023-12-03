"use client";
import { useContext, useEffect, useState } from "react";
import { decrypt } from "@/services/ciphers";
import Results from "./results";
import { CipherContext } from "@/app/page";
import { CipherType } from "@/models/ciphers";
// import Results from "./results";

export default function DecodeCipherForm() {
    const { cipher } = useContext(CipherContext);

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState({
        [cipher]: ""
    });

    const railFenceCeasarPerm = CipherType.PermCesarRailFence + "key";
    const [input, setInput] = useState({
        content: {
            [cipher]: ""
        },
        key: {
            [cipher]: "",
            [railFenceCeasarPerm]: ["", ""] as [string, string]
        }
    });

    const onClickGiaiMa = async () => {
        try {
            if (!input.content || !input.key || Number(input.key) <= 0) return alert("Vui lòng nhập đầy đủ thông tin");
            setLoading(true);
            const permCesarRailFenceKeys = (input.key[railFenceCeasarPerm] as [string, string]).map((value) =>
                parseInt(value)
            ) as [number, number];
            const value = await decrypt({
                cipher_text: input.content[cipher],
                key:
                    cipher == CipherType.PermCesarRailFence
                        ? permCesarRailFenceKeys
                        : parseInt(input.key[cipher] as string),
                type: cipher
            });

            if (value.cipher_text) {
                setResult({
                    ...result,
                    [cipher]: value.plain_text
                });
            }
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

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
    }, [cipher]);

    function renderKeyInput() {
        switch (cipher) {
            case CipherType.PermCesarRailFence:
                return (
                    <div className="flex">
                        <input
                            min="0"
                            required
                            value={input.key[railFenceCeasarPerm][0]}
                            onChange={(value) => {
                                setInput({
                                    ...input,
                                    key: {
                                        ...input.key,
                                        [railFenceCeasarPerm]: [
                                            value.currentTarget.value,
                                            input.key[railFenceCeasarPerm][1]
                                        ]
                                    }
                                });
                            }}
                            type="number"
                            className="mt-4 mr-2 w-24 input input-bordered input-sm input-error"
                            placeholder="Khóa Ceasar"
                        />
                        <input
                            min="0"
                            required
                            value={input.key[railFenceCeasarPerm][1]}
                            onChange={(value) => {
                                setInput({
                                    ...input,
                                    key: {
                                        ...input.key,
                                        [railFenceCeasarPerm]: [
                                            input.key[railFenceCeasarPerm][0],
                                            value.currentTarget.value
                                        ]
                                    }
                                });
                            }}
                            type="number"
                            className="mt-4 mr-2 w-24 input input-bordered input-sm input-error"
                            placeholder="Khóa Rail Fence"
                        />
                    </div>
                );
            default:
                return (
                    <input
                        min="0"
                        required
                        value={input.key[cipher]}
                        onChange={(value) => {
                            setInput({
                                ...input,
                                key: {
                                    ...input.key,
                                    [cipher]: value.currentTarget.value
                                }
                            });
                        }}
                        type="number"
                        className="mt-4 w-24 input input-bordered input-sm input-error"
                        placeholder="Khóa"
                    />
                );
        }
    }

    return (
        <div className=" py-4 ">
            <h3 className="card-title"> Giải mã </h3>
            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    onClickGiaiMa();
                }}
                className="py-4 form-control">
                <textarea
                    required
                    onChange={(event) => {
                        setInput({
                            ...input,
                            content: {
                                ...input.content,
                                [cipher]: event.currentTarget.value
                            }
                        });
                    }}
                    value={input.content[cipher]}
                    className="textarea h-24 textarea-bordered textarea-sm textarea-error"
                    placeholder="Nội dung"
                />

                {renderKeyInput()}
                <div className="mt-4">
                    <button
                        disabled={loading}
                        type="submit"
                        className="btn btn-sm btn-error text-white">
                        Giải mã
                    </button>
                </div>
            </form>
            {result[cipher] && (
                <Results
                    loading={loading}
                    results={result[cipher]}
                />
            )}
        </div>
    );
}
