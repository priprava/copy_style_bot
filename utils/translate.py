from googletrans import Translator

async def translate(text: str):
    async with Translator() as translator:
        result = await translator.translate(text, dest="en")
        return result