import Image from "next/image";
import CipherProvider from "./ciphers/cipher";

export default function Home() {
    return (
        <>
            <div className="px-20 bg-slate-100 navbar bg-base-100 fixed z-50">
                <div className="flex-none">
                    <a className="btn btn-square btn-ghost">
                        <Image 
                            color="#fff"
                            alt="Bách Khoa Cipher"
                            width="24"
                            height="24"
                            className="inline-block w-5 h-5 stroke-current"
                            src="/760px-HCMUT_official_logo.png"
                        />
                    </a>
                </div>
                <div className="flex-1">
                    <a className="btn btn-ghost normal-case text-xl">Bách Khoa Cipher</a>
                </div>
            </div>
            <main className="flex bg-slate-50 flex-col py-16 px-20">
                <CipherProvider />
            </main>
        </>
    );
}
