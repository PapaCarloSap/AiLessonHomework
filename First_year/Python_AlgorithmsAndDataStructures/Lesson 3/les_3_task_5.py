'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

source_list = [random.randint(-99, 99) for _ in range(random.randint(10,21))]
print(source_list)
pos_find_items = list()
min_item = None
for index, current_item in enumerate(source_list):
    if min_item == None and current_item < 0:
        pos_find_items.append(index)
        min_item = current_item
        continue
    if min_item != None and current_item > min_item and current_item<  0:
        pos_find_items.clear()
        pos_find_items.append(index)
        min_item = current_item
    elif min_item != None and current_item == min_item:
        pos_find_items.append(index)
    
print(f'Значение: {min_item}\t Позиции: {pos_find_items}')
