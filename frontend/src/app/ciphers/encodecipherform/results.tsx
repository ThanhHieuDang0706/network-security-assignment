import CopyButton from "@/components/CopyButton";

export default function Results(props: { results: string; loading: boolean }) {
    const element = Array.isArray(props.results) ? (
        props.results.map((result, index) => <p key={result + index}>{result}</p>)
    ) : (
        <p className="inline text-base">{props.results}</p>
    );

    if (props.loading)
        return (
            <div className="animate-pulse">
                <span className="text-blue-400 font-semibold">Kết quả: </span>
                <span className="loading loading-dots loading-sm"></span>
            </div>
        );

    return (
        <div className="flex flex-wrap">
            <div className="text-blue-400 font-semibold whitespace-pre-line">Kết quả: 
                <CopyButton results={props.results} />
            </div>
            <div>
                <pre className="whitespace-pre-wrap">{element}</pre>
            </div>
        </div>
    );
}
