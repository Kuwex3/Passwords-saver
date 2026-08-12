import asyncio
from aiohttp import ClientSession
from aiohttp_socks import ProxyConnector
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

from bot.config import token as bot_token
from bot.save_pass_handler import router as save_router
from bot.ip_giver import router as ip_router

dp = Dispatcher()

dp.include_router(save_router)
dp.include_router(ip_router)

@dp.message(Command("start"))
async def main(message: Message):
    await message.answer("Hello")

async def start():
    connector = ProxyConnector.from_url("socks5://127.0.0.1:1080")
    
    async with ClientSession(connector=connector) as client_session:
        session = AiohttpSession(session=client_session)
        bot = Bot(token=bot_token, session=session)
        
        print("Bot ready!")
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())