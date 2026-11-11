import asyncio
import os
import httpx

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()

async def ask_api(question: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            os.getenv('API_URL') + '/ask',
            json={'question': question},
            timeout=60,
        )
        data = response.json()
        return data['answer']



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!')


@dp.message(F.text)
async def answer_question(message: Message):
    answer = await ask_api(message.text)
    await message.answer(answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())