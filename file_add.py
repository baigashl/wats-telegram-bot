import json
from fille_get import make_request


async def add_db(id_data):
    s = await make_request()
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': 'application/json',
    }
    product_url2 = 'https://kaspi.kz/merchantcabinet/api/order/details/%7Bstatus%7D/'+str(id_data)

    request_data = s.get(
        product_url2,
        headers=headers2,
        cookies=s.cookies.get_dict()
    )

    with open('my_product_detail.json', 'w', encoding='utf-8') as my_json:
        json.dump(request_data.json(), my_json, ensure_ascii=False, indent=4)