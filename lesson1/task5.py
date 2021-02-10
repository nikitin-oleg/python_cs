"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']
args = [args1, args2]
for arg in args:
    subproc_ping = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(line)
        print(line.decode('utf-8'))
        subproc_ping.terminate()

# Установлена ОС Linux, по-этому обошлось по простому варианту
