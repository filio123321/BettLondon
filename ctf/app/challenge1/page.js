// app/challenge1/page.js
"use client"

import { useSearchParams, useRouter } from "next/navigation"
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

import { PARTIAL_CODES } from "@/utils/partialCodes"

export default function Challenge1Page() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const role = searchParams.get("role") || "guest"

  const isAdmin = role.toLowerCase() === "admin"
  const partialCode = isAdmin ? PARTIAL_CODES.challenge1 : null

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-xl bg-neutral-800 p-6">
        <CardHeader>
          <CardTitle className="text-xl">Challenge 1: URL Манипулация</CardTitle>
          <CardDescription className="text-neutral-400">
            Променете URL параметъра <code>?role=???</code>, за да получите достъп
          </CardDescription>
        </CardHeader>
        
        {isAdmin ? (
          <div className="mt-4 space-y-2">
            <p>Поздравления, {role}! Вие успяхте!</p>
            <p>Вашият първи частичен код: <strong>{partialCode}</strong></p>
            <Button onClick={() => router.push("/challenge2")}>
              Отидете към Challenge 2
            </Button>
          </div>
        ) : (
          <div className="mt-4 space-y-2">
            <p className="text-red-400">Достъп отказан. В момента сте с роля "{role}".</p>
            <p>Подсказка: Проверете параметъра в URL-а. 😉</p>
          </div>
        )}
      </Card>
    </main>
  )
}
