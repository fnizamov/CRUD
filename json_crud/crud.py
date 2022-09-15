import json
from json.decoder import JSONDecodeError
from settings import DB

from datetime import datetime


""" 
list_ = [
    {
        "id": 1,
        "title": "LG",
        "price": 1000,
        "description": "Life Is Good",
        "date_created": "24.08.22 19:05"
    },
    {
        "id": 2,
        "title": "Samsung",
        "price": 1000,
        "description": "Samsung",
        "date_created": "24.08.22 19:05"
    }
] 
"""


def get_all_data():
    with open(DB) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []



def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название '),
        'price': int(input('Введите цену ')),
        'description': input('Введите описание '),
        'date_created': datetime.now().strftime('%d.%m.%Y %H:%M')
    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(DB, 'w') as f:
        json.dump(json_data, f, indent=4)


def get_data_by_id():
    id_ = input('Введите id ')
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
    return 'Not found'


def delete_data():
    id_ = input('Введите id ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)


def update():
    id_ = input('Введите id ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите название ') or obj['title']
            obj['price'] = int(input('Введите цену ')) or obj['price']
            obj['description'] = input('Введите описание ') or obj['description']
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)

