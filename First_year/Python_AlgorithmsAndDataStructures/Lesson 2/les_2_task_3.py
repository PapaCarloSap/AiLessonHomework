"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, надо вывести 6843.
"""

user_data = input('Input numbers: ')
result = ''
for i in range(len(user_data),0,-1):
    result = result + user_data[i-1]
print(f'Result: {result}')