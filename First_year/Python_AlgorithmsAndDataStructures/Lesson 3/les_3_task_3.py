'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

source_list = [random.randint(0, 9) for _ in range(20)]
print(source_list)
pos_max_list = list()
pos_min_list = list()
max_value = 0
min_value = 0
for pos, item in enumerate(source_list):
    if len(pos_max_list)>0 and max_value == item:
        pos_max_list.append(pos)
    elif len(pos_max_list)>0 and max_value < item:
        pos_max_list.clear()
        pos_max_list.append(pos)
        max_value = item
    elif len(pos_min_list)>0 and min_value == item:
        pos_min_list.append(pos)
    elif len(pos_min_list)>0 and min_value > item:
        pos_min_list.clear()
        pos_min_list.append(pos)
        min_value = item
    elif len(pos_min_list)==0 and  len(pos_max_list)==0:
        pos_min_list.append(pos)
        pos_max_list.append(pos)
        max_value = item
        min_value = item

for pos in pos_max_list:
    source_list[pos] = min_value

for pos in pos_min_list:
    source_list[pos] = max_value

print(source_list)