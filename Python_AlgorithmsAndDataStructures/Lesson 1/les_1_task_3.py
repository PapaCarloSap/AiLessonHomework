'''
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''
#%%
import random

start_int_num, finish_int_num = map(int, input('Введите диапазон целых чисел: (start; finish)').split(';'))
start_float_num, finish_float_num = map(float, input('Введите диапазон вещественных чисел: (start; finish)').split(';'))
start_sym, finish_sym = input('Введите диапазон сиволов: (start; finish)').split(';')

random_int = random.randint(start_int_num, finish_int_num)
random_float = random.uniform(start_float_num, finish_float_num)
random_sym = chr(random.randint(ord(start_sym), ord(finish_sym)))

print(f'Случайное целое число: {random_int}')
print(f'Случайное вещественное число: {random_float}')
print(f'Случайный символ: {random_sym}')

# %%
