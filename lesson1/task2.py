"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""
var1 = b'class'
var2 = b'function'
var3 = b'method'

my_list = [var1, var2, var3]

for var in my_list:
    print(type(var), var, len(var), sep=', ')
