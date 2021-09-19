'''
Определить, какое число в массиве встречается чаще всего.
'''
import random

source_list = [random.randint(0, 9) for _ in range(random.randint(10,31))]
print(source_list)
num_find = 0
find_items = list()
for item_find in source_list:
    num_find_buffer = 0
    for item in source_list:
        if item_find == item:
            num_find_buffer +=1
        
    if num_find_buffer>num_find:
        num_find = num_find_buffer
        find_items.clear()
        find_items.append(item_find)
    elif num_find_buffer == num_find and item_find not in find_items:
        find_items.append(item_find)

print(f'Наибольшее число: {find_items}  Количество: {num_find}')
