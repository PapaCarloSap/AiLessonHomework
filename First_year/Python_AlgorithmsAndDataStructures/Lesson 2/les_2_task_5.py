"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

num_element=0
result =''
for index_ascii in range(32, 128):
    if num_element == 10:
        num_element=0
        print(result)
        result = ''
    else:
        result = result + '{0}-{1}\t'.format(index_ascii, chr(index_ascii))
        num_element+=1
if result != '':
    print(result)
    