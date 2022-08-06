import io
import os
from aiogram import Bot, types
from aiogram.utils import executor
import psycopg2
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from db_data import db_commands
from whatsapp import messenger
from fille_get import try_api
from config_data import bot, storage, dp
from file_data import add_data
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from oauth2client.service_account import ServiceAccountCredentials
import gsheets
import requests



button4 = KeyboardButton('Добавить на Базу данных')
button5 = KeyboardButton('Отправить на Whatsapp')

markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button4, button5)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # await try_api()
    # await add_data()
    await message.reply("Welcome", reply_markup=markup3)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("ok")


@dp.message_handler(content_types=['text'])
async def echo_message(message: types.Message):
    if message.text == 'Отправить на Whatsapp':
        options = Options()
        options.headless = False

        # options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        options.add_argument("user-data-dir=~/Library/Application Support/Google/Chrome/Default")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        DRIVER_PATH = os.path.join(dir_path, 'config/chromedriver')
        print(DRIVER_PATH)
        await try_api()
        await add_data()
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        # driver.minimize_window()
        for i in range(1):
            if await db_commands.get_data_whatsapp() != []:
                await messenger("https://web.whatsapp.com/send?phone=", await db_commands.get_data_whatsapp(), driver)
            await message.reply("Отправлен")
            driver.quit()

    if message.text == 'Добавить на Базу данных':
        await message.reply("Немного подождите")
        pdkey = "test.json"

        SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        CREDS = ServiceAccountCredentials.from_json_keyfile_name(pdkey, SCOPE)

        access_token = CREDS.create_delegated(CREDS._service_account_email).get_access_token().access_token
        url = "https://docs.google.com/spreadsheets/export?id=1KMUNG2eppvyUzgMAwGYSSZlLSqsXJfVU1nlukfqOMFs&exportFormat=xlsx"

        res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

        with open("output.xlsx", 'wb') as f:
            f.write(res.content)
        await db_commands.add_user("output.xlsx")
        await message.reply("Добавил")


if __name__ == '__main__':
    executor.start_polling(dp)
