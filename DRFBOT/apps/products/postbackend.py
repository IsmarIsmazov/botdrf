import logging
from aiogram import Bot, types
from aiogram.utils import executor
from decouple import config

API_KEY = config("API_KEY")
bot = Bot(token=API_KEY)
logging.basicConfig(level=logging.INFO)

async def send_notification(chat_id, message_text):
    await bot.send_message(chat_id, message_text)


