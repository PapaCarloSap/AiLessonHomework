user_data = input('Введите список значений через пробел: ')
item_list = user_data.rstrip().split(' ')
if len(item_list) % 2 != 0:
    print('Не четное значение в массиве')
    exit(0)
for index in range(0,len(item_list), 2):
    buffer = item_list[index]
    item_list[index] = item_list[index+1]
    item_list[index+1] = buffer
print(f'Результат: {item_list}')
