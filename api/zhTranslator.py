import asyncio
from googletrans import Translator

async def translate_text(srctext):
    async with Translator() as translator:
        srclang = await translator.detect(srctext)
        destlang = input("Lang: ")
        result = await translator.translate(srctext, src=srclang.lang, dest=destlang)
        print(f"==>   {result.text}")

asyncio.run(translate_text(input("Text: ")))
