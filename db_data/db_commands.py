import io
import xlrd
import openpyxl
import datetime
from openpyxl_image_loader import SheetImageLoader
from config_data import bot
from db_data.db import connection
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


def read():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT sku FROM users_db_tel_bot;""")
        data = cursor.fetchall()
        sku_data = []
        for i in data:
            sku_data.append(i[0])
        return sku_data


async def add_user(state):
    file = state
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    pxl_doc = openpyxl.load_workbook(file)
    sheet_image = pxl_doc['Sheet1']
    image_loader = SheetImageLoader(sheet_image)
    columns_number = sheet.ncols
    raw_number = sheet.nrows
    first = False
    second = False
    third = False
    fourth = False
    fifth = False
    first_o = False
    second_o = False
    third_o = False
    fourth_o = False
    fifth_o = False

    first_t = False
    second_t = False
    third_t = False
    fourth_t = False
    fifth_t = False

    for i in range(raw_number):
        if i == 0:
            continue
        sku = sheet.cell_value(i, 0)
        if str(sku) not in read():
            product_name = sheet.cell_value(i, 1)

            file_name1 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                first = True
                image = image_loader.get('C' + str(i + 1))

                image.save(file_name1)
            except ValueError:
                first = False
            file_name2 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                second = True
                image = image_loader.get('D' + str(i + 1))

                image.save(file_name2)
            except ValueError:
                second = False
            file_name3 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                third = True
                image = image_loader.get('E' + str(i + 1))

                image.save(file_name3)
            except ValueError:
                third = False
            file_name4 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fourth = True
                image = image_loader.get('F' + str(i + 1))

                image.save(file_name4)
            except ValueError:
                fourth = False
            file_name5 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fifth = True
                image = image_loader.get('G' + str(i + 1))

                image.save(file_name5)
            except ValueError:
                fifth = False

            file_name6 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                first_o = True
                image = image_loader.get('H' + str(i + 1))

                image.save(file_name6)
            except ValueError:
                first_o = False
            file_name7 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                second_o = True
                image = image_loader.get('I' + str(i + 1))

                image.save(file_name7)
            except ValueError:
                second_o = False
            file_name8 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                third_o = True
                image = image_loader.get('J' + str(i + 1))

                image.save(file_name8)
            except ValueError:
                third_o = False
            file_name9 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fourth_o = True
                image = image_loader.get('K' + str(i + 1))

                image.save(file_name9)
            except ValueError:
                fourth_o = False
            file_name10 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fifth_o = True
                image = image_loader.get('L' + str(i + 1))

                image.save(file_name10)
            except ValueError:
                fifth_o = False
            file_name11 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'

            try:
                first_t = True
                image = image_loader.get('M' + str(i + 1))

                image.save(file_name11)
            except ValueError:
                first_t = False
            file_name12 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                second_t = True
                image = image_loader.get('N' + str(i + 1))

                image.save(file_name12)
            except ValueError:
                second_t = False
            file_name13 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                third_t = True
                image = image_loader.get('O' + str(i + 1))

                image.save(file_name13)
            except ValueError:
                third_t = False
            file_name14 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fourth_t = True
                image = image_loader.get('P' + str(i + 1))

                image.save(file_name4)
            except ValueError:
                fourth_t = False
            file_name15 = f'may_images/image{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.jpg'
            try:
                fifth_t = True
                image = image_loader.get('Q' + str(i + 1))

                image.save(file_name15)
            except ValueError:
                fifth_t = False

            with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO users_db_tel_bot(sku, product_name, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14, image15) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                        (
                            # id,
                            sku,
                            product_name,
                            file_name1 if first else None,
                            file_name2 if second else None,
                            file_name3 if third else None,
                            file_name4 if fourth else None,
                            file_name5 if fifth else None,
                            file_name6 if first_o else None,
                            file_name7 if second_o else None,
                            file_name8 if third_o else None,
                            file_name9 if fourth_o else None,
                            file_name10 if fifth_o else None,
                            file_name11 if first_t else None,
                            file_name12 if second_t else None,
                            file_name13 if third_t else None,
                            file_name14 if fourth_t else None,
                            file_name15 if fifth_t else None,
                        )
                    )
                    print("Добавил")
        elif str(sku) in read():
            print("Уже есть")


async def sql_read(message):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM users_db_tel_bot;""")
        data = cursor.fetchall()
        for i in data:
            if i[1] == message.from_user.id:
                print(i[0])
                d = str(i[0])
                await bot.send_document(message.from_user.id, i[-1])


async def sql_del(data):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users_db_tel_bot WHERE id = (%s)", (data))


async def sql_read_del(message):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM users_db_tel_bot;""")
        data = cursor.fetchall()
        for i in data:
            if i[1] == message.from_user.id:
                print(i[0])
                d = str(i[0])
                await bot.send_message(message.from_user.id,
                                       f'id: {i[0]},\nname: {i[-2]},\nadmin_id: {i[1]},\nadmin: {i[2]}')


# Whatsapp


async def add_deatil(data):
    id_order = data['id']
    user_name = data['name']
    phone = data['phone']
    product = data['product']
    sku = data['sku']
    status = data['status']
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO info_user(id_order, user_name, phone, product, status, sku, send) VALUES (%s, %s, %s, %s, %s,  %s, %s);", (id_order, user_name, phone, product, status, sku, '0'))


async def get_data_message_sku2():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM info_user;")
        data = cursor.fetchall()
        p = []
        for i in data:
            if i[-1]!='1':
                p.append(i[-2])
    return p

async def get_data():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM list;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


async def get_data_info():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM info_user;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


async def get_data_info2():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM info_user;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


async def get_data_info3():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM info_user;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


async def get_data_whatsapp():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT phone, sku, id_order, status, send FROM info_user;")
        for i in cursor.fetchall():
            print(i)
            if i[-1] != '1':
                data.append([i[0], i[1], str(i[2]), i[3]])
    return data


async def get_data_message():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users_db_tel_bot;")
        data = cursor.fetchall()
        p = {}
        for i in data:
            p[i[1]] = []
            for n in i[2:]:
                if n != None:
                    p[i[1]].append(n)
    return p


async def get_data_message_sku():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users_db_tel_bot;")
        data = cursor.fetchall()
        p = []
        for i in data:
            p.append(i[1])
    return p


async def get_data_message_send():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM info_user;")
        data = cursor.fetchall()
        p = []
        for i in data:
            if i[-1] != '1':
                p.append(i[0])
    return p


async def update_table(id_order):
    id_order = int(id_order)
    print(id_order)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE info_user SET send = '1' WHERE id_order = %s;", (id_order,))
