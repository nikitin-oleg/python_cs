"""
    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
    Проверить работу программы через вызов функции write_to_csv().
"""

import csv
from chardet.universaldetector import UniversalDetector

files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
file_csv = 'main_data.csv'
with open(f'{file_csv}', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    f_n_writer.writerow(main_data)


def char_detector(file):
    detector = UniversalDetector()
    with open(f'{file}', 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']


def get_data(file):
    os_prod_list = ''
    os_name_list = ''
    os_code_list = ''
    os_type_list = ''
    with open(f'{file}', 'r', encoding=f"{char_detector(file)}") as f:
        f_reader = csv.reader(f, delimiter=":")
        for row in f_reader:
            if row[0] == 'Изготовитель системы':
                os_prod_list += row[1].strip()
            elif row[0] == 'Название ОС':
                os_name_list += row[1].strip()
            elif row[0] == 'Код продукта':
                os_code_list += row[1].strip()
            elif row[0] == 'Тип системы':
                os_type_list += row[1].strip()
    data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    return data


def write_to_csv(name, file):
    with open(f'{name}', 'a') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        f_writer.writerow(get_data(file))


if __name__ == "__main__":
    for file in files_list:
        write_to_csv(file_csv, file)
