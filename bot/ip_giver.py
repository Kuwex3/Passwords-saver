from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

import requests

router = Router()

@router.message(Command("ip"))
async def give_ip(msg: Message):
    ip = requests.get("https://api.ipify.org/")
    print(ip.text)
    await msg.answer(f"{ip.text}")