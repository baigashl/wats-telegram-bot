import json
from db_data import db_commands
from file_add import add_db


async def add_data():
    with open("my_product_1.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)

        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info2():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")

            else:
                print("Уже есть")

    with open("my_product_2.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)
        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    print((data2['orderId']))
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")

            else:
                print("Уже есть")

    with open("my_product_3.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)
        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")

            else:
                print("Уже есть")


async def add_data2():
    with open("my_product_1.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)

        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info3():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")

            else:
                print("Уже есть")

    with open("my_product_2.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)
        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    print((data2['orderId']))
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")

            else:
                print("Уже есть")

    with open("my_product_3.json", "r", encoding='utf-8') as data:
        data_j1 = json.load(data)
        for i in data_j1['orders']:
            if int(i['orderNumber']) not in await db_commands.get_data_info():
                await add_db(i['orderNumber'])
                with open("my_product_detail.json", "r", encoding='utf-8') as data2:
                    data2 = json.load(data2)
                    db = {}
                    db['id'] = int(data2['orderId'])
                    db['name'] = data2['purchaserFirstName']
                    db['phone'] = data2['purchaserPhoneNumber']
                    db['product'] = data2['products'][0]['masterProduct']['name']
                    db['sku'] = data2['products'][0]['sku']
                    db['status'] = data2['deliveryMode']
                await db_commands.add_deatil(db)
                print("Добавил")
            else:
                print("Уже есть")
