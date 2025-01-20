// app/challenge4/page.js
"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import { PARTIAL_CODES } from "@/utils/partialCodes"

export default function Challenge4Page() {
  const router = useRouter()
  const [solution, setSolution] = useState("")
  const [error, setError] = useState(false)

  const handleSubmit = () => {
    if (solution === PARTIAL_CODES.challenge4) {
      router.push("/submit")
    } else {
      setError(true)
    }
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-xl bg-neutral-800 p-6">
        <CardHeader>
          <CardTitle className="text-xl">Challenge 4: Геолокация</CardTitle>
          <CardDescription className="text-neutral-400">
            Намерете това по-необичайно място чрез reverse image search или улики.
          </CardDescription>
        </CardHeader>
        <div className="mt-4 space-y-2">
          {error && <p className="text-red-400">Грешно решение. Опитайте отново!</p>}
          <img 
            src="/placeholder-landmark.jpg" 
            alt="Landmark" 
            className="w-full h-auto rounded border border-neutral-700"
          />
          <Input 
            placeholder="Въведете открития частичен код..."
            value={solution}
            onChange={(e) => setSolution(e.target.value)}
          />
          <Button onClick={handleSubmit}>Изпрати</Button>
        </div>
      </Card>
    </main>
  )
}
