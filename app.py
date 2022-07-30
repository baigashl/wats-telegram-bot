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




button4 = KeyboardButton('/Добавить_на_DataBase')
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


class FSMAdmin(StatesGroup):
    document = State()


class FSMAdminDel(StatesGroup):
    id = State()


@dp.message_handler(commands='Добавить_на_DataBase', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id:
        await FSMAdmin.document.set()
        await message.reply('Загрузить документ.')


@dp.message_handler(content_types=['document'], state=FSMAdmin.document)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id:
        async with state.proxy() as data:
            data['document'] = message.document.file_id
            file_name = message.document.file_name
            id = message.from_user.id
            first_name = (message.from_user.first_name)
            user = {"id": id, "first_name": first_name}
            with io.BytesIO() as file_in_io:
                await message.document.download(destination_file=file_in_io)
                with open("output.xlsx", "wb") as f:
                    f.write(file_in_io.getbuffer())
                print('bye')
                await db_commands.add_user(user, "output.xlsx", file_name)
            # await db_commands.add_user(user, data['document'], file_name)
            await message.reply("Документ добавлен")

        await state.finish()


@dp.message_handler(commands=['menu'])
async def space_menu(message: types.Message):
    for i in range(1):
        await db_commands.sql_read(message)


@dp.message_handler(commands=['whatsapp'])
async def space_whatsapp(message: types.Message):
    for i in range(1):
        await messenger("https://web.whatsapp.com/send?phone=", await db_commands.get_data_whatsapp())
        await message.reply("Отправлен")


@dp.message_handler(commands=['id'])
async def space_menu(message: types.Message):
    for i in range(1):
        await db_commands.sql_read_del(message)


@dp.message_handler(commands='del', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id:
        await FSMAdminDel.id.set()
        await message.reply("Укажите  id документа.")


@dp.message_handler(state=FSMAdminDel.id)
async def load_id(message: types.Message, state: FSMContext):
    if message.from_user.id:
        async with state.proxy() as data:
            data['id'] = message.text
            await db_commands.sql_del(data['id'])
            await message.reply("Домент del")
        await state.finish()


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


if __name__ == '__main__':
    executor.start_polling(dp)
