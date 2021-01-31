"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet.universaldetector import UniversalDetector

test_text = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w', encoding="cp1251") as f:
    for itm in test_text:
        f.write(f'{itm} \n')

detector = UniversalDetector()
with open('test_file.txt', 'rb') as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)

with open('test_file.txt', 'r', encoding=f"{detector.result['encoding']}") as fr:
    with open('test_file_utf8.txt', 'w', encoding='utf-8') as fw:
        for line in fr:
            fw.write(line[:-1] + '\r\n')
