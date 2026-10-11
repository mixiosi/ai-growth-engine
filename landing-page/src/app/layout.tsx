import type { Metadata } from "next";
import Script from "next/script";
import "./globals.css";

export const metadata: Metadata = {
  title: "The Autonomous AI Growth Engine | 100 Prompts & SOPs for B2B Tech",
  description:
    "100 Battle-Tested AI Prompts, 4 Production SOPs, and Automated Distribution Architectures for B2B Tech Founders and Revenue Leaders.",
  keywords: [
    "AI Prompts",
    "B2B SaaS Growth",
    "Autonomous Agents",
    "Outbound Automation",
    "SOPs",
    "Zernio SDK",
    "Revenue Engineering",
  ],
  openGraph: {
    title: "The Autonomous AI Growth Engine",
    description:
      "Scale B2B revenue and traffic with 100 production AI prompts, SOPs, and automated social distribution.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <Script src="https://gumroad.com/js/gumroad.js" strategy="afterInteractive" />
      </head>
      <body className="bg-slate-950 text-slate-100 antialiased selection:bg-indigo-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
