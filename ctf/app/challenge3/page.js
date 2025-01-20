// app/challenge3/page.js
"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import { PARTIAL_CODES } from "@/utils/partialCodes"

export default function Challenge3Page() {
  const router = useRouter()
  const [solution, setSolution] = useState("")
  const [error, setError] = useState(false)

  const handleSubmit = () => {
    if (solution === PARTIAL_CODES.challenge3) {
      router.push("/challenge4")
    } else {
      setError(true)
    }
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-xl bg-neutral-800 p-6">
        <CardHeader>
          <CardTitle className="text-xl">Challenge 3: Скрито в изображение (Стеганография / EXIF)</CardTitle>
          <CardDescription className="text-neutral-400">
            Научете повече за ELSYS: Имаме две емблематични събития всяка година, организирани от 
            ученици за ученици: <strong>HackTues</strong> и <strong>TuesFest</strong>.
          </CardDescription>
        </CardHeader>
        <div className="mt-4 space-y-2">
          {error && <p className="text-red-400">Грешно решение. Опитайте отново!</p>}
          <p className="text-neutral-200">
            Прегледайте това изображение и вижте дали има скрита информация (EXIF данни, стеганография).
          </p>
          <img 
            src="/placeholder-stego.jpg" 
            alt="Stego Puzzle" 
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
