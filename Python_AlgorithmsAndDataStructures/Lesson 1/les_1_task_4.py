'''
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''
#%%
sym_first = input('Введите стартовую букву')
sym_second = input('Введите конечную букву')

position_sym_first = ord(sym_first)-96
position_sym_second = ord(sym_second)-96
number_letter = abs(position_sym_first - position_sym_second)-1

print(f'Позиция буквы \'{sym_first}\' = {position_sym_first}')
print(f'Позиция буквы \'{sym_second}\' = {position_sym_second}')
print(f'Количество букв между буквами \'{sym_first}\' и \'{sym_second}\' = {number_letter}')

# %%
