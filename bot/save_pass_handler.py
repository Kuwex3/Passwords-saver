from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.passwords_uploader import save

router = Router()

@router.message(Command("!!"))
async def save_handler(message: Message):
    clean_pass = message.text.replace(" ", "", 1).replace("/", "", 1).replace("!", "", 2)
    await save(clean_pass)