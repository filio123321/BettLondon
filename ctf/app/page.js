// app/page.js
"use client"

import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { useRouter } from "next/navigation"

export default function HomePage() {
  const router = useRouter()

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4">
      <Card className="w-full max-w-md p-6 bg-neutral-800">
        <CardHeader>
          <CardTitle className="text-2xl">Добре дошли в нашата мини-CTF игра!</CardTitle>
          <CardDescription className="text-neutral-400">
            Зловредни хакери са откраднали важна информация от ELSYS. 
            Придвижете се през предизвикателствата, за да я възстановите!
          </CardDescription>
        </CardHeader>
        <div className="mt-4 flex justify-end">
          <Button onClick={() => router.push("/challenge1")}>
            Отидете към Challenge 1
          </Button>
        </div>
      </Card>
    </main>
  )
}
