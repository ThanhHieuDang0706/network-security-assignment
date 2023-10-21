export default  function Results(props: { results: string | string[] }) {
    const element = Array.isArray(props.results) ? props.results.map((result, index) => (
        <p key={result + index}>{result}</p>
    )) : <p className="inline text-base">{props.results}</p>;

    return <div className="mt-4">
        <span className="text-blue-400 font-semibold">Kết quả: </span>
        {element}
    </div>;
}