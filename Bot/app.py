from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

API_KEY = config('API_KEY')
storage = MemoryStorage()

bot = Bot(token=API_KEY)
dp = Dispatcher(bot=bot, storage=storage)