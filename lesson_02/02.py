"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
 Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
 количество (quantity), цена (price), покупатель (buyer), дата (date).
  Функция должна предусматривать запись данных в виде словаря в файл orders.json.
   При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(data: list):
    print(data)
    with open('orders.json', 'w', encoding='utf-8', newline='') as orders_file:
        s = '{"orders": ' + json.dumps(data, indent=4) + '}'
        orders_file.write(s)


write_order_to_json([{
    'item': 'Стул',
    'quantity': 1,
    'price': 10,
    'buyer': 'Стульщик',
    'date': '05.12.21'
},{
    'item': 'Стол',
    'quantity': 2,
    'price': 20,
    'buyer': 'Стольщик',
    'date': '06.12.21'
},{
    'item': 'Гроб',
    'quantity': 3,
    'price': 30,
    'buyer': 'Шкафник',
    'date': '08.12.21'
}])
