import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import file_data
import asyncio
from db_data.db_commands import get_data_whatsapp, get_data_message, get_data_message_sku, update_table, \
    get_data_message_send, get_data_message_sku2

base_dir = os.path.dirname(os.path.realpath(__file__))


async def whatsapp_render(contact, data, driver):
    try:
        get = await get_data_message()
        if data[1] in await get_data_message_sku():
            data_sku = get[data[1]]
            driver.get(contact)
            await asyncio.sleep(20)
            message_content = f"Здравствуйте,\n Благодарим вас за заказ!"

            inp_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
            input_box = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, inp_xpath)))
            input_box.send_keys(message_content + Keys.ENTER)

            attachment_box = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@title = "Attach"]'))
            )
            attachment_box.click()

            await asyncio.sleep(1)
            h = ""
            if len(data_sku) >= 2:

                h += os.path.join(base_dir, str(data_sku[1]))
                for i in data_sku[2:]:
                    h += '\n' + os.path.join(base_dir, str(i))

            if h != "":
                image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(h)
                await asyncio.sleep(5)
                send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                send_button.click()
            await update_table(data[-1])

        await asyncio.sleep(2)
    except IndexError as e:
        driver.quit()
        print(e)


async def messenger(url, data, driver):
    try:
        # contacts = ["700619706"]
        phone = []
        for i in data[0]:
            phone.append(i[0])
        for n in range(len(data)):
            contact = url+data[n][0]
            # contact = url + contacts[0]
            if str(data[n][1]) in await get_data_message_sku2():
                await whatsapp_render(contact, data[n], driver)
    except Exception as e:
        print(e)
        os._exit(0)
