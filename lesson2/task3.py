"""
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом:
allow_unicode = True;
    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

data = {
    'список': ['msg_1', 'msg_2', 'msg_3'],
    'целое число': 122,
    'вложенный словарь': {
        'евро': '1000€',
        'йена': '1000¥',
        'рубль': '1000₽'
    }
}


def write_to_yaml(data):
    with open('file.yaml', 'w') as f_n:
        yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)


def read_from_yaml():
    with open('file.yaml', 'r') as f_n:
        data = yaml.load(f_n, Loader=yaml.FullLoader)
        return data


if __name__ == "__main__":
    write_to_yaml(data)
    read_from_yaml()
