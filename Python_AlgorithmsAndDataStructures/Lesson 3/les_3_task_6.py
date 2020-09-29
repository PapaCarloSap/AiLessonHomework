'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

source_list = [random.randint(0, 99) for _ in range(random.randint(10,11))]
print(source_list)
min_item = None
max_item = None
min_positions = list()
max_positions = list()
for index, item in enumerate(source_list):
    if min_item == None:
        min_item = item
        max_item = item
        min_positions.append(index)
        max_positions.append(index)
        continue

    if min_item>item:
        min_item = item
        min_positions.clear()
        min_positions.append(index)
        continue

    if min_item==item:
        min_positions.append(index)

    if max_item<item:
        max_item = item
        max_positions.clear()
        max_positions.append(index)
        continue

    if max_item==item:
        max_positions.append(index)
        continue

result = 0
start = 0
end = 0
if min_positions[0]< max_positions[len(max_positions)-1]:
    start = min_positions[0]
    end = max_positions[len(max_positions)-1]
else:
    start = max_positions[len(max_positions)-1]
    end = min_positions[0]

for index in range(start+1, end):
    cur_item = source_list[index]
    if(cur_item == min_item or cur_item == max_item):
        continue
    result += cur_item

print(f'Сумма {result}')