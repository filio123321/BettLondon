// app/submit/page.js
"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { PARTIAL_CODES } from "@/utils/partialCodes"

export default function SubmitPage() {
  const router = useRouter()
  
  const [code1, setCode1] = useState("")
  const [code2, setCode2] = useState("")
  const [code3, setCode3] = useState("")
  const [code4, setCode4] = useState("")
  const [error, setError] = useState(false)

  const handleSubmit = () => {
    if (
      code1 === PARTIAL_CODES.challenge1 &&
      code2 === PARTIAL_CODES.challenge2 &&
      code3 === PARTIAL_CODES.challenge3 &&
      code4 === PARTIAL_CODES.challenge4
    ) {
      router.push("/success")
    } else {
      setError(true)
    }
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-xl bg-neutral-800 p-6">
        <CardHeader>
          <CardTitle className="text-xl">Финален етап</CardTitle>
          <CardDescription className="text-neutral-400">
            Въведете четирите частични кода, за да получите наградата си!
          </CardDescription>
        </CardHeader>
        <div className="mt-4 space-y-4">
          {error && <p className="text-red-400">Някой от кодовете е грешен. Опитайте пак!</p>}

          <div>
            <p>Challenge 1:</p>
            <Input value={code1} onChange={(e) => setCode1(e.target.value)} />
          </div>
          <div>
            <p>Challenge 2:</p>
            <Input value={code2} onChange={(e) => setCode2(e.target.value)} />
          </div>
          <div>
            <p>Challenge 3:</p>
            <Input value={code3} onChange={(e) => setCode3(e.target.value)} />
          </div>
          <div>
            <p>Challenge 4:</p>
            <Input value={code4} onChange={(e) => setCode4(e.target.value)} />
          </div>
          <Button onClick={handleSubmit}>Изпрати</Button>
        </div>
      </Card>
    </main>
  )
}
