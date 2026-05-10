import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Matiks Content OS",
  description: "AI-native Content Operating System — Multi-channel Instagram management at scale",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased bg-[#050a14] text-slate-200 min-h-screen noise-overlay grid-pattern">
        {children}
      </body>
    </html>
  )
}
