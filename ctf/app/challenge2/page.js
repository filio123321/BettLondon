// app/challenge2/page.js
"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import { PARTIAL_CODES } from "@/utils/partialCodes"

export default function Challenge2Page() {
  const router = useRouter()
  const [solution, setSolution] = useState("")
  const [error, setError] = useState(false)

  const handleSubmit = () => {
    if (solution === PARTIAL_CODES.challenge2) {
      router.push("/challenge3")
    } else {
      setError(true)
    }
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-xl bg-neutral-800 p-6">
        <CardHeader>
          <CardTitle className="text-xl">Challenge 2: Многократно кодиране + Шифър на Цезар</CardTitle>
          <CardDescription className="text-neutral-400">
            Тук ще поставите вашето Base64/Цезар съдържание.
          </CardDescription>
        </CardHeader>
        <div className="mt-4 space-y-2">
          {error && <p className="text-red-400">Грешно решение. Опитайте отново!</p>}
          <p className="text-neutral-200">
            Пример: Разкрийте този текст, който изглежда Base64 кодиран 
            и след това прилагайте шифър на Цезар!
          </p>
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
