"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
    Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
    Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json

# без этого кода (строки 13 - 15) при каждом запуске программы в файл будут добавляться новые записи, код приводит
# .json файл в исходное состояние
data = {"orders": []}
with open('orders.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, )


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'товар': item,
        'количество': quantity,
        'цена': price,
        'покупатель': buyer,
        'дата': date
    }

    with open('orders.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        data['orders'].append(order)

    with open('orders.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return data


if __name__ == "__main__":
    write_order_to_json('lamp', '12', '1500', 'John', '10.02.2021')
    write_order_to_json('lamp2', '10', '1520', 'Smith', '11.12.2021')
    write_order_to_json('lamp3', '15', '1500', 'Ann', '12.12.2021')
    write_order_to_json('lamp4', '18', '1500', 'Jek', '13.12.2021')
