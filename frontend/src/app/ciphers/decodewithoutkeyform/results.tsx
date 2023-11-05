import { useEffect, useState } from "react";

interface Props {
    loading: boolean;
    results: {
        [key: string]: string;
    };
}

export default function Results(props: Props) {
    const [displayedResult, setDisplayedResult] = useState<Array<{ key: number; plain_text: string }>>([]);
    const [pageNumber, setPageNumber] = useState("1");

    const [itemsPerPage, setItemsPerPage] = useState(10);
    const maxPageNumber = Math.ceil(displayedResult.length / Number(itemsPerPage));

    useEffect(() => {
        setDisplayedResult(
            Object.entries(props.results).map(([key, plain_text]) => ({
                key: Number(key),
                plain_text
            }))
        );
    }, [props.results]);

    if (props.loading) {
        return (
            <div className="text-center">
                <span className="loading loading-dots loading-md"></span>
            </div>
        );
    }

    if (displayedResult.length === 0) {
        return (
            <div className="text-center">
                <p className="text-md">Không có kết quả</p>
            </div>
        );
    }

    return (
        <>
            <div className="overflow-x-auto mb-4 text-center">
                <table className="table">
                    {/* head */}
                    <thead>
                        <tr>
                            <th>Rail</th>
                            <th>Bản rõ</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* row 1 */}
                        {displayedResult.map((result, index) => {
                            if (index >= (Number(pageNumber) - 1) * Number(itemsPerPage) && index < Number(pageNumber) * Number(itemsPerPage)) {
                                return (
                                    <tr key={result.key}>
                                        <td>{result.key}</td>
                                        <td>{result.plain_text}</td>
                                    </tr>
                                );
                            }
                        })}
                    </tbody>
                </table>
            </div>

            <div className="flex justify-center items-center">
                <label className="mr-2">Số dòng hiển thị</label>
                <input  
                    value={itemsPerPage}
                    type="number"
                    min="0"
                    onChange={(e) => {
                        if (e.currentTarget.value != "") 
                            setItemsPerPage(parseInt(e.currentTarget.value.replace(/^0+/, "")));
                        else 
                            setItemsPerPage(0);
                        e.currentTarget.value  = itemsPerPage.toString();
                    }}
                    className="border border-gray-300 rounded-md px-2 py-1 w-20"
                />
                <label
                    htmlFor="page number"
                    className="ml-2">
                    Trang
                </label>
                <input
                    type="number"
                    min="1"
                    max={maxPageNumber}
                    name="page number"
                    onChange={(e) => setPageNumber((e.target.value))}
                    className="border border-gray-300 rounded-md px-2 py-1 w-20 ml-2"
                />&nbsp;
                / {maxPageNumber}
            </div>
        </>
    );
}
