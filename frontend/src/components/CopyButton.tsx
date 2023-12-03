import { faCopy } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useState } from "react";

export default function CopyButton(props: { results: string }) {
    const [tooltip, setTooltip] = useState("Copy kết quả");
    return (
        <button onMouseLeave={() => {
            setTooltip("Copy kết quả");
        }} onClick={() => {
            navigator.clipboard.writeText(props.results);
            setTooltip("Đã copy kết quả");
        }} className="border-none px-4 bg-transparent tooltip" data-tip={tooltip}>
            <FontAwesomeIcon
                icon={faCopy}
                className="text-blue-400"
            />
        </button>
    );
}