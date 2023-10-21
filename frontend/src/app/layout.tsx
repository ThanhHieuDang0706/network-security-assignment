import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "Bách Khoa Cipher",
    description: "Simple cipher tool for encrypting and decrypting text",
    viewport: "width=device-width, initial-scale=1",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en" data-theme="bumblebee">
            <body className={inter.className}>{children}</body>
        </html>
    );
}
