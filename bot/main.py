from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

from bot.config import token as bot_token

from bot.save_pass_handler import router as save_router

import asyncio

bot = Bot(token=bot_token)
dp = Dispatcher()

dp.include_router(save_router)

@dp.message(Command("start"))
async def main(message: Message):
    await message.answer("Hello!")

async def start():
    print("Bot ready!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())