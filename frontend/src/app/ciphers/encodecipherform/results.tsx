import { useContext } from "react";
import { CipherContext } from "../cipher";


export default function Results(props: { results: string, loading: boolean }) {
    const element = Array.isArray(props.results) ? props.results.map((result, index) => (
        <p key={result + index}>{result}</p>
    )) : <p className="inline text-base">{props.results}</p>;

    if (props.loading) return (
        <div className="animate-pulse">
            <span className="text-blue-400 font-semibold">Kết quả: </span>
            <p className="inline text-base">Đang xử lý...</p>
        </div>
    );

    return <div className="">
        <span className="text-blue-400 font-semibold whitespace-pre-line">Kết quả: </span>
        <pre className="whitespace-pre-wrap">
            {element}
        </pre>
    </div>;
}