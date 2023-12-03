import CopyButton from "@/components/CopyButton";

export default function Results(props: { results: string, loading: boolean }) {
    const element = Array.isArray(props.results) ? props.results.map((result, index) => (
        <p key={result + index}>{result}</p>
    )) : <p className="inline text-base">{props.results}</p>;

    if (props.loading) return (
        <div className="max-w-sm animate-pulse">
            <div className="h-2 bg-gray-200 rounded-full dark:bg-gray-700"></div>
        </div>
    );

    return <div className="flex flex-wrap">
        <div className="text-blue-400 font-semibold whitespace-pre-line">Kết quả:
            <CopyButton results={props.results} />
        </div>
        <div>
            <pre className="whitespace-pre-wrap">{element}</pre>
        </div>
    </div>
}