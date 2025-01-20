// app/layout.js
import './globals.css'
import { Inter } from 'next/font/google'
import { cn } from '@/lib/utils' // If you are using shadcn’s utility for className merges

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Mini CTF App',
  description: 'Mini-CTF challenges by ELSYS at Bett',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={cn(inter.className, 'bg-neutral-900 text-neutral-50')}>
        {children}
      </body>
    </html>
  )
}
