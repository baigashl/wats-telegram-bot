from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine, Column, Integer, Boolean, String
from sqlalchemy.orm import scoped_session, sessionmaker
from aiogram import Bot, types, Dispatcher

# TOKEN = "5482480288:AAEdWp-RgUMYhB40sRGzPR5Rm0zg5KzJKIo"
TOKEN = "5498775460:AAHfpZkhhKAyWxPW_31m_W2zH6_y-ghdAAs"
ip = "localhost"
user = "owner_db"
password = "123"
db_name = "data_telegram"

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

PG_URL = f'postgresql: //{user}:{password}@{ip}/{db_name}'

