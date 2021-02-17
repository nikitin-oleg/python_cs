"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

var1 = 'разработка'
var2 = 'администрирование'
var3 = 'protocol'
var4 = 'standard'

my_list = [var1, var2, var3, var4]

for var in my_list:
    var = var.encode('utf-8')
    print(type(var), var, len(var), sep=', ')
    var = var.decode('utf-8')
    print(type(var), var, len(var), sep=', ')
